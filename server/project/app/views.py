from django.shortcuts import render
from rest_framework import generics, mixins, permissions, exceptions, response
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

class MessageList(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = (
            permissions.IsAuthenticated,
    )

    def perform_create(self, serializer):
        chat = get_object_or_404(Chat, id=self.kwargs['chat_id'])
        profile = self.request.user.profile
        instance = serializer.save(author=profile, chat=chat)

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



class StartChat(APIView):
    permission_classes = (
            permissions.IsAuthenticated,
    )

    def post(self, request, user_id, format=None):
        print(user_id)
        return Response()

