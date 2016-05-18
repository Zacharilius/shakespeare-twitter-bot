import os
import secret
import tweepy

class TwitterAPI:
    def __init__(self):
        consumer_key = "zYHhJVjVQqXdri098oEzxqLBU"
        consumer_secret = consumer_secret
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = "4248624134-gjIafbmt06dTTW9CRQOf9tE4KCOpPWIYHLZRqQX"
        access_token_secret = access_token_secret
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(status=message)

if __name__ == "__main__":
    twitter = TwitterAPI()
    twitter.tweet("A horse! A horse! My kingdom for a horse!")
