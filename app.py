import os
from flask import Flask, request, abort

from biblebot.tweeter import Tweeter

app = Flask(__name__)

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
        return tweet_all()
    abort(401)
