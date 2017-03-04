from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^chat/(?P<chat_id>[0-9]+)/messages/$', views.MessageList.as_view(), name='message_list'),
]
