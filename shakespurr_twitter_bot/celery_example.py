import atexit
from apscheduler.schedulers.blocking import BlockingScheduler
from celery import Celery
from celery.schedules import crontab
from flask import Flask, Blueprint, abort, jsonify, request, session
import os
import tweepy
from os import path, environ
import json
import settings


def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

app = Flask(__name__)
app.config.from_object(settings)

celery = make_celery(app)
celery.conf.update(
    CELERYBEAT_SCHEDULE = {
        'every-minute': {
            'task': 'executing.now',
            'schedule': crontab(minute='*/1'),
            'args': (),
        },
    }
)


@celery.task(name="executing.now")
def executing_now():
    print('executing.now')

@celery.task(name="tasks.add")
def add(x, y):
    return x + y

@app.route("/test")
def hello_world(x=16, y=16):
    x = int(request.args.get("x", x))
    y = int(request.args.get("y", y))
    res = add.apply_async((x, y))
    context = {"id": res.task_id, "x": x, "y": y}
    result = "add((x){}, (y){})".format(context['x'], context['y'])
    goto = "{}".format(context['id'])
    return jsonify(result=result, goto=goto)

@app.route("/test/result/<task_id>")
def show_result(task_id):
    retval = add.AsyncResult(task_id).get(timeout=1.0)
    return repr(retval)


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


if __name__ == "__main__":
    port = int(environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)


# if __name__ == "__main__":
#     ...
    # twitter = TwitterAPI()
    # twitter.tweet("A horse! A horse! My kingdom for a horse!")
