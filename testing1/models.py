from distutils.command.upload import upload
import email
from django.db import models


class userModel(models.Model):
    userName = models.CharField(max_length=200)
    email=models.TextField()
    

    