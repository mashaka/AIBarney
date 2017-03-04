from django.contrib import admin
from .models import *


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    pass

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Queue)
class QueueAdmin(admin.ModelAdmin):
    pass

@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    pass



