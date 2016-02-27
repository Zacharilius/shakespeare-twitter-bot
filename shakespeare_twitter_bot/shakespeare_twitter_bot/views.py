from django.http import HttpResponse
from django.shortcuts import render


def shakespeare_twitter_bot(request):
    return render(request, "shakespeare_twitter_bot/index.html", {})


def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")
