from django.shortcuts import render
from rest_framework import generics, mixins, permissions, exceptions, response
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub, SubscribeListener
 
pnconfig = PNConfiguration()
pnconfig.publish_key = 'pub-c-8465dadc-3bc2-40be-a68d-16110286f809'
pnconfig.subscribe_key = 'sub-c-51962ec8-0100-11e7-8437-0619f8945a4f'
pubnub = PubNub(pnconfig)
 

class MessageList(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = (
            permissions.IsAuthenticated,
    )

    def perform_create(self, serializer):
        chat = get_object_or_404(Chat, id=self.kwargs['chat_id'])
        profile = self.request.user.profile
        instance = serializer.save(author=profile, chat=chat)
        user_to = [p.user.id for p in chat.users.all() if p.id != profile.id][0]
        channel = str(user_to) + '_' + str(chat.id)
        msg = serializer.to_representation(instance)
        print(channel)
        print(msg)
        pubnub.publish().channel(channel).message(msg).sync()

    def get_queryset(self):
        chat = get_object_or_404(Chat, id=self.kwargs['chat_id'])
        return Message.objects.filter(chat=chat).order_by('-add_time')

class UserList(generics.ListAPIView):
    serializer_class = UserListSerializer

    permission_classes = (
            permissions.IsAuthenticated,
    )

    def get_queryset(self):
        return Profile.objects.exclude(user=self.request.user)

class MeUser(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer

    permission_classes = (
            permissions.IsAuthenticated,
    )

    def get_object(self):
        return self.request.user.profile



class StartChat(generics.CreateAPIView):
    serializer_class = ChatSerializer
    permission_classes = (
            permissions.IsAuthenticated,
    )

    def perform_create(self, serializer):
        user = get_object_or_404(User, id=self.kwargs['user_id']).profile
        profile = self.request.user.profile
        chat = Chat.objects.filter(
                users=user).filter(users=profile)
        if chat.count() == 0:
            instance = serializer.save()
            instance.users.add(profile)
            instance.users.add(user)
            instance.save()
        else:
            raise Http404()

