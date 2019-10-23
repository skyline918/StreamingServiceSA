from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Video(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(to='User', on_delete=models.SET_NULL, null=True)
    url = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField(auto_now=True, blank=True)
    description = models.TextField(default='')
    category = models.ForeignKey(to='VideoCategory', on_delete=models.SET_NULL, null=True)
    location = models.FileField(upload_to="videos")


class VideoCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)


class Comment(models.Model):
    message = models.TextField(null=False)
    date = models.DateTimeField(auto_now=True, blank=True)
    video = models.ForeignKey(to='Video', null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(to='User', null=False, on_delete=models.CASCADE)


class VideoStat(models.Model):
    liked = models.BooleanField(null=False)
    date = models.DateTimeField(auto_now=True, blank=True)
    video = models.ForeignKey(to='Video', null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(to='User', null=False, on_delete=models.CASCADE)


class CDN(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
