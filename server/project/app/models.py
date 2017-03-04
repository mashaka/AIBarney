from django.db import models
from django.contrib.auth_models import User

class Profile(models.Model):
    user = models.OneToOneField(User)
    avatar_url = models.URLField(max_length=200,null=True,blank=True)

class UserData(models.Model):
    user = models.OneToOneField(User)
    data = TextField(null=True,default=None)

class Chat(models.Model):
    firt_user = models.ForeignKey(Profile)
    second_user = models.ForeignKey(Profile)

class Message(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Profile)
    add_time = models.DateTimeField(auto_now_add=True)
    chat_id = models.ForeignKey(Chat)
