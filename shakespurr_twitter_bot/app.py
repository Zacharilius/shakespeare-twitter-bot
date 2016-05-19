import datetime
from flask import Flask, request, session
from flask_peewee.db import Database
from flask_peewee.admin import Admin, ModelAdmin
from flask_peewee.auth import Auth
from os import path, environ
from peewee import *
import settings
import tweepy


# ------------------------------------------------------------------------------
# Database Settings

DATABASE = {
    'name': 'shakespurr.db',
    'engine': 'peewee.SqliteDatabase'
}

DEBUG = True

SECRET_KEY = settings.SECRET_KEY


# ------------------------------------------------------------------------------
# Flask App Settings

app = Flask(__name__)
app.config.from_object(__name__)

db = Database(app)

auth = Auth(app, db)
admin = Admin(app, auth)


# ------------------------------------------------------------------------------
# Flask Models

class ShakespeareQuote(db.Model):
    quote = TextField()
    created = DateTimeField(default=datetime.datetime.now)
    source_url = TextField()


class ShakespeareQuoteAdmin(ModelAdmin):
    columns = ('quote', 'created')


# ------------------------------------------------------------------------------
# Flask Views

@app.route('/')
def index():
    return 'index'


@app.route('/tweet')
def tweet():
    # twitter = TwitterAPI()
    # twitter.tweet("A horse! A horse! My kingdom for a horse!")
    return 'tweet'


# ------------------------------------------------------------------------------
# Twitter

class TwitterAPI:
    def __init__(self):
        consumer_key = "zYHhJVjVQqXdri098oEzxqLBU"
        consumer_secret = settings.consumer_secret
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = "4248624134-gjIafbmt06dTTW9CRQOf9tE4KCOpPWIYHLZRqQX"
        access_token_secret = settings.access_token_secret
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(status=message)


# ------------------------------------------------------------------------------
# Run Server

if __name__ == "__main__":
    ShakespeareQuote.create_table(fail_silently=True)
    auth.User.create_table(fail_silently=True)

    admin.register(ShakespeareQuote, ShakespeareQuoteAdmin)
    admin.setup()

    app.run(
        host='0.0.0.0',
        port=int(environ.get("PORT", 5000))
    )
