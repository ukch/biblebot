import os
from flask import Flask, request, abort

from biblebot.tweeter import DebugTweeter, Tweeter

app = Flask(__name__)

def debug_tweet_all():
    html = ['<h1 style="color: red">ATTENTION: DEBUG MODE IS ON</h1>',
            '<p>(This means that no tweets have actually been sent.)</p>',
            '<p>The following tweets <em>would</em> have been sent:</p>']
    for tweet in DebugTweeter().tweet_all():
        html.append('<blockquote>{}</blockquote>'.format(tweet))
    return os.linesep.join(html)


def tweet_all():
    kwargs = {}
    for key in ['consumer_key', 'consumer_secret', 'access_token_key',
                'access_token_secret']:
        env_key = 'twitter_{}'.format(key)
        kwargs[key] = os.getenv(env_key)
        if kwargs[key] is None:
            return 'Please set "{}" in Heroku'.format(env_key)
    num = Tweeter(**kwargs).tweet_all()
    return 'Sent {} tweet(s)'.format(num)


@app.route('/')
def cron():
    api_key = os.getenv('api_key')
    if api_key is None:
        return 'Please set an API key in Heroku'
    if request.args.get('key') and request.args.get('key') == api_key:
        if app.debug:
            return debug_tweet_all()
        return tweet_all()
    abort(401)
