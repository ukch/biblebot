from datetime import date, timedelta
import logging

from dateutil.parser import parse as dateutil_parse
from store import redis
import twitter

from biblebot.constants import TEMPLATE, SHORT_TEMPLATE
from biblebot.data import readings
from biblebot.url_service import URL_SHORTENERS


class LastTweetedDateNotSet(Exception):
    pass


class Tweeter(object):

    def __init__(self, consumer_key, consumer_secret, access_token_key,
                 access_token_secret):
        self.api = twitter.Api(consumer_key=consumer_key,
                               consumer_secret=consumer_secret,
                               access_token_key=access_token_key,
                               access_token_secret=access_token_secret)

    def _get_last_tweeted(self):
        if not hasattr(self, '_last_tweeted_date'):
            data = redis.get('last_tweeted_date')
            if data is None:
                raise LastTweetedDateNotSet()
            self._last_tweeted_date = dateutil_parse(data).date()
        return self._last_tweeted_date

    def _set_last_tweeted(self, value):
        self._last_tweeted_date = value
        redis.set('last_tweeted_date', value)

    last_tweeted_date = property(_get_last_tweeted, _set_last_tweeted)

    def get_relevant_dates(self, until):
        one_day = timedelta(days=1)
        start_date = self.last_tweeted_date + one_day
        end_date = until + one_day
        for n in xrange(int((end_date - start_date).days)):
            yield start_date + timedelta(n)

    def try_send_tweet(self, tweet, url_shortener):
        if not tweet.startswith('>'):
            url = url_shortener.get_url(tweet)
            tweet = '{} {}'.format(tweet, url)
        final_tweet = TEMPLATE.format(tweet)
        if len(final_tweet) > 140:
            final_tweet = SHORT_TEMPLATE.format(tweet)
            if len(final_tweet) > 140:
                final_tweet = tweet
        self.api.PostUpdate(final_tweet)

    def send_tweets(self, dt):
        tweets = readings.get(dt.month, {}).get(dt.day, ())
        for tweet in tweets:
            for url_shortener in URL_SHORTENERS:
                try:
                    self.try_send_tweet(tweet, url_shortener)
                except twitter.TwitterError, e:
                    try:
                        data, = e.args
                        data, = data
                    except ValueError:
                        raise e
                    # 'Status contains malware'
                    if data.get("code") == 188:
                        msg = "URL shortener '{}' flagged as malware"
                        logging.warn(msg.format(url_shortener.URL_PATTERN))
                else:
                    break
            else:
                raise RuntimeError("All shorteners flagged as spam")
        return len(tweets)

    def get_today(self):
        return date.today()

    def tweet_all(self, force_today=False):
        today = self.get_today()
        tweeted = 0
        if force_today:
            # We use force_today to forcibly set last_tweeted_date
            dates = [today]
        else:
            dates = self.get_relevant_dates(today)
        for dt in dates:
            tweeted += self.send_tweets(dt)
        # We only do this once to reduce IO overhead
        self.last_tweeted_date = today
        return tweeted


class _DebugApi(list):

    def PostUpdate(self, data):
        self.append(data)


class DebugTweeter(Tweeter):

    def __init__(self):
        self.api = _DebugApi()

    def get_today(self):
        if self.force_day:
            return self.force_day
        return super(DebugTweeter, self).get_today()

    def tweet_all(self, *args, **kwargs):
        self.force_day = kwargs.pop('force_day', None)
        if self.force_day is not None:
            kwargs['force_today'] = True
        super(DebugTweeter, self).tweet_all(*args, **kwargs)
        return list(self.api)
