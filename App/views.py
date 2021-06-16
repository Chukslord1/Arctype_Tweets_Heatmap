from django.shortcuts import render
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
from django.http import HttpResponse
from . models import Tweets



# Create your views here.
consumer_key="api_key"
consumer_secret="api_secret_key"
access_token="access_token"
access_token_secret="access_token_secret"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)
username=["Cristiano","BarackObama","rihanna","elonmusk","TheRock"]




def index(request):
    tweet_count = 0
    for i in username:
        for status in Cursor(auth_api.user_timeline, id=i).items():
            tweet_count = tweet_count + 1
            if status.created_at.year == 2021 and status.created_at.month == 5:
                tweets_save= Tweets.objects.create(username=i,tweet_number=tweet_count,created_at=status.created_at.date(),retweet_count=status.retweet_count)
                tweets_save.save()
            else:
                continue

    return HttpResponse('<h1>Loaded Tweets Data</h1>')
