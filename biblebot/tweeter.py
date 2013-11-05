from datetime import date#, timedelta

import twitter

from biblebot.constants import TEMPLATE
from biblebot.data import readings


class Tweeter(object):

    def __init__(self, consumer_key, consumer_secret, access_token_key,
                 access_token_secret):
        self.api = twitter.Api(consumer_key=consumer_key,
                               consumer_secret=consumer_secret,
                               access_token_key=access_token_key,
                               access_token_secret=access_token_secret)

    def get_relevant_dates(self, until):
        # TODO proper date range
        # see http://stackoverflow.com/questions/1060279/
        #     iterating-through-a-range-of-dates-in-python
        return [until]

    def send_tweets(self, dt):
        tweets = readings.get(dt.month, {}).get(dt.day)
        for tweet in tweets:
            self.api.PostUpdate(TEMPLATE.format(tweet))
        return len(tweets)

    def tweet_all(self):
        today = date.today()
        tweeted = 0
        for dt in self.get_relevant_dates(today):
            tweeted += self.send_tweets(dt)
        return tweeted


class _DebugApi(list):

    def PostUpdate(self, data):
        self.append(data)


class DebugTweeter(Tweeter):

    def __init__(self):
        self.api = _DebugApi()

    def tweet_all(self):
        super(DebugTweeter, self).tweet_all()
        return list(self.api)
