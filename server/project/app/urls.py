from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^chat/(?P<chat_id>[0-9]+)/messages/$', views.MessageList.as_view(), name='message_list'),
    url(r'^users/$', views.UserList.as_view(), name='user_list'),
    url(r'^users/me/$', views.MeUser.as_view(), name='user_me'),
    url(r'^chat/start/(?P<user_id>[0-9]+)/$', views.StartChat.as_view(), name='start_chat'),
]
