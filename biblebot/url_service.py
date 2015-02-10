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


class ReflyUrlShortener(UrlShortener):

    URL_PATTERN = 'http://ref.ly/{}'

    def format_tweet(self, tweet):
        tweet = tweet.replace(":", ".")
        return super(ReflyUrlShortener, self).format_tweet(tweet)


class VrefUrlShortener(UrlShortener):

    """
    This is not as powerful as para.ms (and we need to jump through a few more
    hoops) but it probably can't ever be used by spammers.
    """

    URL_PATTERN = 'http://vref.me/{}'

    def format_tweet(self, tweet):
        # More than one chapter
        if tweet.count(":") == 2:
            beginning, end = tweet.split("-")
            book, beginning = beginning.rsplit(" ", 1)
            beginning_chap, unused = beginning.split(":")
            end_chap, unused = end.split(":")
            full_refs = [
                "{book} {chap}:1-200".format(book=book, chap=chap)
                for chap in range(int(beginning_chap) + 1, int(end_chap))
            ]
            beginning = "{book} {ref}-200".format(book=book, ref=beginning)
            end = "{book} {ref}".format(book=book, ref=end)
            refs = [beginning] + full_refs + [end]
            tweet = "{}".format(";".join(refs))
        tweet = tweet.replace(":", ".")
        return super(VrefUrlShortener, self).format_tweet(tweet)


URL_SHORTENERS = [ReflyUrlShortener(), VrefUrlShortener()]
