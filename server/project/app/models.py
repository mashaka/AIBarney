from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User)
    avatar_url = models.URLField(max_length=200,null=True,blank=True)

class UserData(models.Model):
    user = models.OneToOneField(User)
    data = models.TextField(null=True,default=None)

class Chat(models.Model):
    users = models.ManyToManyField(Profile)

class Message(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Profile)
    add_time = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(Chat, related_name='messages')
