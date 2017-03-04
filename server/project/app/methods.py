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


def download_data(user):
    fb = get_connection(user)
    data = dict()
    data['music'] = fb.get_object('me/music',
            fields='genre,cover,events'
                '{place,name,start_time,end_time}',
            limit=1000)
    data['movies'] = fb.get_object('me/movies',
            fields='genre,cover,name',
            limit=1000)
    data['books'] = fb.get_object('me/books', limit=1000)
    data['general'] = fb.get_object('me',
            fields='education,hometown,languages,work')

