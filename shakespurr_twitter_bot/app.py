import datetime
from flask import Flask, render_template, request, session
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
    is_tweeted = BooleanField(default=False)

    def set_tweeted(self):
        self.is_tweeted = True
        self.save()


class ShakespeareQuoteAdmin(ModelAdmin):
    columns = ('quote', 'created', 'source_url', 'is_tweeted')


# ------------------------------------------------------------------------------
# Flask Views

@app.route('/')
def index():
    return render_template('shakespurrean_twitter_bot.html')


@app.route('/shakespurrean_twitter_bot')
def tweet():
    return render_template('shakespurrean_twitter_bot.html')


# ------------------------------------------------------------------------------
# Run Server

if __name__ == "__main__":
    ShakespeareQuote.create_table(fail_silently=True)
    auth.User.create_table(fail_silently=True)

    admin.register(ShakespeareQuote, ShakespeareQuoteAdmin)
    admin.setup()

    if 'liveconsole' not in gethostname():
        app.run(
            host='0.0.0.0',
            port=int(environ.get("PORT", 5000))
        )
