from django.shortcuts import render
from django.http import HttpResponse


def home_view(request, *args, **kwargs):
  return HttpResponse(f'Hello')


def tweet_detail_view(request, tweet_id,*args, **kwargs):
  return HttpResponse(f'Hello {tweet_id}')