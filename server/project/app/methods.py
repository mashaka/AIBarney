from .models import *

import facebook
facebook.VALID_API_VERSIONS = ['2.8']

def get_token(user):
    return (user.social_auth.get(provider='facebook').
            extra_data['access_token'])

def get_connection(user):
    return facebook.GraphAPI(access_token=get_token(user),
            version='2.8')

def prepare_user(user):
    profile, created = Profile.objects.get_or_create(user=user)
    if created:
        profile.avatar_url = get_connection(user).get_object(
                'me/picture', height=160)['url']
        profile.save()

