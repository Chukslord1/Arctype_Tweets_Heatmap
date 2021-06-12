from django.db import models

# Create your models here.
class Tweets(models.Model):
    tweet_number = models.IntegerField()
    created_at = models.DateField()
    retweeted= models.TextField()

    def __str__(self):
        return self.tweet_number
