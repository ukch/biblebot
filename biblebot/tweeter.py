from datetime import date#, timedelta

from biblebot.constants import TEMPLATE
from biblebot.data import readings

class Tweeter(object):

    def get_relevant_dates(self, until):
        # TODO proper date range
        # see http://stackoverflow.com/questions/1060279/
        #     iterating-through-a-range-of-dates-in-python
        return [until]

    def send_tweets(self, dt):
        tweets = readings.get(dt.month, {}).get(dt.day)
        for tweet in tweets:
            print TEMPLATE.format(tweet)
        return len(tweets)

    def tweet_all(self):
        today = date.today()
        tweeted = 0
        for dt in self.get_relevant_dates(today):
            tweeted += self.send_tweets(dt)
        return tweeted
