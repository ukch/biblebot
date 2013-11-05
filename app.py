import os
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/')
def cron():
    api_key = os.getenv('api_key')
    if api_key is None:
        return 'Please set an API key in Heroku'
    if request.args.get('key') and request.args.get('key') == api_key:
        return 'api key correct'
    abort(401)
