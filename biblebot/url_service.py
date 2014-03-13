import urllib

class UrlShortener(object):

    URL_PATTERN = NotImplemented

    def format_tweet(self, tweet):
        return urllib.quote(tweet.replace(' ', ''))

    def get_url(self, tweet):
        safe_tweet = self.format_tweet(tweet)
        if self.URL_PATTERN is NotImplemented:
            raise NotImplementedError()
        return self.URL_PATTERN.format(safe_tweet)


class ParamsUrlShortener(UrlShortener):

    URL_PATTERN = 'http://para.ms/bible/{}'


URL_SHORTENERS = [ParamsUrlShortener()]
