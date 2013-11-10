import cPickle
from datetime import date, timedelta
import os

import twitter

from biblebot.constants import TEMPLATE, LAST_TWEETED_FILENAME
from biblebot.data import readings


class PickleFileDoesNotExist(Exception):
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
            if not os.path.exists(LAST_TWEETED_FILENAME):
                raise PickleFileDoesNotExist(LAST_TWEETED_FILENAME)
            with open(LAST_TWEETED_FILENAME) as fh:
                self._last_tweeted_date = cPickle.load(fh)
        return self._last_tweeted_date

    def _set_last_tweeted(self, value):
        self._last_tweeted_date = value
        with open(LAST_TWEETED_FILENAME, 'w') as fh:
            cPickle.dump(value, fh)

    last_tweeted_date = property(_get_last_tweeted, _set_last_tweeted)

    def get_relevant_dates(self, until):
        one_day = timedelta(days=1)
        start_date = self.last_tweeted_date + one_day
        end_date = until + one_day
        for n in xrange(int((end_date - start_date).days)):
            yield start_date + timedelta(n)

    def send_tweets(self, dt):
        tweets = readings.get(dt.month, {}).get(dt.day)
        for tweet in tweets:
            self.api.PostUpdate(TEMPLATE.format(tweet))
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
