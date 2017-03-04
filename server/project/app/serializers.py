from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
                     max_length=30,
                     allow_blank=True,
                     source='user.first_name'
                 )
    last_name = serializers.CharField(
                    max_length=30,
                    allow_blank=True,
                    source='user.last_name'
                )
    class Meta:
        model = Profile
        fields = ('id', 'first_name', 'last_name',
                  'avatar_url')

class MessageSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(method_name='get_mauthor')
    def get_mauthor(self, post):
        return ProfileSerializer(**{'context': self.context}).to_representation(post.author)
    class Meta:
        model = Message
        fields = '__all__'

class ChatSerializer(serializers.ModelSerializer):
    last_message = serializers.SerializerMethodField()
    
    def get_last_message(self, chat):
        return (MessageSerializer(**{'context': self.context}).
            to_representation(chat.messages.
                order_by('-add_time').first()))

    class Meta:
        model = Chat
        fields = ('last_message', 'id')

class UserListSerializer(ProfileSerializer):
    has_chat = serializers.SerializerMethodField()
    chat = serializers.SerializerMethodField()

    def get_has_chat(self, profile):
        return False

    def get_chat(self, profile):
        return None
    class Meta:
        model = Profile
        fields = ('id', 'first_name', 'last_name',
                  'avatar_url', 'has_chat', 'chat')


