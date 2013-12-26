import os
import sys
import traceback

from dateutil.parser import parse as dateutil_parse
from flask import Flask, request, abort

from biblebot.tweeter import DebugTweeter, Tweeter, LastTweetedDateNotSet

app = Flask(__name__)

def debug_tweet_all(force_today=False, force_day=None):
    html = ['<h1 style="color: red">ATTENTION: DEBUG MODE IS ON</h1>',
            '<p>(This means that no tweets have actually been sent.)</p>',
            '<p>The following tweets <em>would</em> have been sent:</p>']
    for tweet in DebugTweeter().tweet_all(force_today=force_today,
                                          force_day=force_day):
        html.append('<blockquote>{}</blockquote>'.format(tweet))
    return os.linesep.join(html)


def tweet_all(force_today=False):
    kwargs = {}
    for key in ['consumer_key', 'consumer_secret', 'access_token_key',
                'access_token_secret']:
        env_key = 'twitter_{}'.format(key)
        kwargs[key] = os.getenv(env_key)
        if kwargs[key] is None:
            return 'Please set "{}" in Heroku'.format(env_key)
    num = Tweeter(**kwargs).tweet_all(force_today=force_today)
    return 'Sent {} tweet(s)'.format(num)


@app.route('/')
def cron():
    api_key = os.getenv('api_key')
    if api_key is None:
        return 'Please set an API key in Heroku'
    if request.args.get('key') and request.args.get('key') == api_key:
        kwargs = {'force_today': 'force_today' in request.args}
        if app.debug:
            func = debug_tweet_all
            day = request.args.get('day', None)
            if day is not None:
                day = dateutil_parse(day).date()
            kwargs['force_day'] = day
        else:
            func = tweet_all
        try:
            return func(**kwargs)
        except LastTweetedDateNotSet:
            return 'Unable to calculate date of last tweet'
        except:
            traceback.print_exc(file=sys.stderr)
            raise
    abort(401)
