BibleTweetBot
=============

This app was written so as to tweet the contents of my church's 'Bible in a
year' plan to the world at large. Feel free to modify it as you see fit.

Usage
-----

* [dev.twitter.com](http://dev.twitter.com) to create an app. Set the
permissions to read/write and generate an access key.
* `heroku create`
* Come up with a local api key so the world at large can't tweet on your behalf
(I recommend a [UUID](http://www.uuidgenerator.net/version1))
* Set your remote settings. Use something like the following:

        heroku config:set twitter_consumer_key=CONSUMER_KEY \
            twitter_consumer_secret=CONSUMER_SECRET \
            twitter_access_token_key=ACCESS_TOKEN \
            twitter_access_token_secret=ACCESS_SECRET api_key=MY_API_KEY
