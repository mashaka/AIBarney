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
