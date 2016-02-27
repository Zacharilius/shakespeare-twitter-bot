from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def twitter_bot(request):
    return HttpResponse("Hello, world. You're at the polls index.")