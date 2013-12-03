from datetime import date, timedelta
import urllib

from dateutil.parser import parse as dateutil_parse
from store import redis
import twitter

from biblebot.constants import TEMPLATE, SHORT_TEMPLATE, URL_PATTERN
from biblebot.data import readings


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

    def send_tweets(self, dt):
        tweets = readings.get(dt.month, {}).get(dt.day, ())
        for tweet in tweets:
            if not tweet.startswith('>'):
                # para.ms doesn't handle whitespace properly
                urlsafe_tweet = urllib.quote(tweet.replace(' ', ''))
                url = URL_PATTERN.format(urlsafe_tweet)
                tweet = '{} {}'.format(tweet, url)
            final_tweet = TEMPLATE.format(tweet)
            if len(final_tweet) > 140:
                final_tweet = SHORT_TEMPLATE.format(tweet)
                if len(final_tweet) > 140:
                    final_tweet = tweet
            self.api.PostUpdate(final_tweet)
        return len(tweets)

    def tweet_all(self, force_today=False):
        today = date.today()
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

    def tweet_all(self, *args, **kwargs):
        super(DebugTweeter, self).tweet_all(*args, **kwargs)
        return list(self.api)
