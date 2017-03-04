from .models import *
import time
import json
import pickle
from decimal import Decimal
import algo
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
        Queue.objects.create(type='fetch', args=str(user.id))
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
    UserData.objects.create(user=user, data=pickle.dumps(data))

STOP = False


def build_input_data(dataa, datab):
    res = []
    res.append(InputData(CategoryType.GENERAL_INFO,
                        dataa['general'],
                        datab['general']))
    return res

def start_chat(chat):
    usera, userb = chat.users.all()[:]
    dataa = pickle.loads(usera.user.userdata.data)
    datab = pickle.loads(userb.user.userdata.data)
    chata = algo.ChatRoom(build_input_data(dataa, datab))
    chatb = algo.ChatRoom(build_input_data(datab, dataa))
    UserData.objects.create(user=usera, chat=chat,
            data=pickle.dumps(chata))
    UserData.objects.create(user=userb, chat=chat,
            data=pickle.dumps(chatb))

def process_queue_item(job):
    if job.type == 'fetch':
        download_data(User.objects.get(id=int(job.args)))
    elif job.type == 'start_chat':
        start_chat(Chat.objects.get(id=int(job.args)))
    else:
        raise Exception('Unknown job type ' + job.type)
    job.done = True
    job.save()

def stop_processing():
    STOP = True

def process_queue(cnt=Decimal('Infinity')):
    while not STOP and cnt > 0:
        sz = Queue.objects.filter(done=False).count()
        print('Queue size:', sz)
        if sz:
            process_queue_item(
                    Queue.objects.filter(done=False).
                        order_by('add_time').first())
        else:
            time.sleep(1)
        cnt -= 1
