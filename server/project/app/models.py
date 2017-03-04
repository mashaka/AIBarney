from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User)
    avatar_url = models.URLField(max_length=200,null=True,blank=True)

    def __str__(self):
        return 'Profile ' + str(self.user.id)

class UserData(models.Model):
    user = models.OneToOneField(User)
    data = models.TextField(null=True,default=None)

    def __str__(self):
        return 'UserData ' + str(self.user.id)


class Chat(models.Model):
    users = models.ManyToManyField(Profile)

    def __str__(self):
        return 'Chat ' + str(self.id)


class Message(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Profile)
    add_time = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(Chat, related_name='messages')

    def __str__(self):
        return 'Message ' + str(self.id) + ' in ' + str(self.chat.id)


