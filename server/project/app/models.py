from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User)
    avatar_url = models.URLField(max_length=200,null=True,blank=True)

    def __str__(self):
        return 'Profile ' + str(self.user.id)

class UserData(models.Model):
    user = models.OneToOneField(User)
    data = models.BinaryField()

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

class Queue(models.Model):
    add_time = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=10)
    args = models.TextField()
    done = models.BooleanField(default=False)
    def __str__(self):
        return '{}({})'.format(self.type, self.args)


class ChatData(models.Model):
    chat = models.ForeignKey(Chat)
    user = models.ForeignKey(User)
    data = models.BinaryField()
    def __str__(self):
        return 'chat:{} user:{}'.format(self.chat.id, self.user.id)
