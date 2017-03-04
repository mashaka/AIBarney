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
    id = serializers.SerializerMethodField()
    def get_id(self, profile):
        return profile.user.id

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
        fields = ('id', 'author', 'text', 'add_time')

class ChatSerializer(serializers.ModelSerializer):
    last_message = serializers.SerializerMethodField(method_name='mget_last_message')
    
    def mget_last_message(self, chat):
        message = chat.messages.order_by('-add_time').first()
        if message is None:
            return None
        else:
            return (MessageSerializer(**{'context': self.context}).
                to_representation())

    class Meta:
        model = Chat
        fields = ('last_message', 'id')

class UserListSerializer(ProfileSerializer):
    has_chat = serializers.SerializerMethodField()
    chat = serializers.SerializerMethodField()

    def get_chat_ins(self, profile):
        return Chat.objects.filter(
                users=self.
                    context['request'].user.profile).filter(
                            users=profile).first()

    def get_chat(self, profile):
        chat = self.get_chat_ins(profile)
        if chat is None:
            return None
        else:
            return (ChatSerializer(**{'context': self.context}).
                to_representation(chat))

    def get_has_chat(self, profile):
        return self.get_chat_ins(profile) is not None

    class Meta:
        model = Profile
        fields = ('id', 'first_name', 'last_name',
                  'avatar_url', 'has_chat', 'chat')

