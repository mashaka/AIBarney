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
            fields='name,genre,cover,events{place,name,start_time,end_time}',
            limit=1000)
    data['movies'] = fb.get_object('me/movies',
            fields='genre,cover,name',
            limit=1000)
    data['books'] = fb.get_object('me/books', limit=1000)
    data['general'] = fb.get_object('me',
            fields='education,hometown,languages,work')
    ud, _ = UserData.objects.get_or_create(user=user)
    ud.data=pickle.dumps(data)
    ud.save()


STOP = False


def build_input_data(dataa, datab):
    res = []
    res.append(algo.InputData(algo.CategoryType.GENERAL_INFO,
                        dataa['general'],
                        datab['general']))
    res.append(algo.InputData(algo.CategoryType.MUSIC,
                        dataa['music'],
                        datab['music']))
    res.append(algo.InputData(algo.CategoryType.BOOKS,
                        dataa['books'],
                        datab['books']))
    res.append(algo.InputData(algo.CategoryType.MOVIES,
                        dataa['movies'],
                        datab['movies']))
    return res

def start_chat(chat):
    usera, userb = chat.users.all()[:]
    dataa = pickle.loads(usera.user.userdata.data)
    datab = pickle.loads(userb.user.userdata.data)
    chata = algo.ChatRoom(build_input_data(dataa, datab))
    chatb = algo.ChatRoom(build_input_data(datab, dataa))
    cda, _ = ChatData.objects.get_or_create(user=usera.user,
                                            chat=chat)
    cda.data=pickle.dumps(chata)
    cda.save()
    cdb, _ = ChatData.objects.get_or_create(user=userb.user,
                                            chat=chat)
    cdb.data=pickle.dumps(chatb)
    cdb.save()

def new_message(msg, tip):
    chata = ChatData.objects.get(user=msg.author.user, chat=msg.chat)
    userb = msg.chat.users.all().exclude(
            user=msg.author.user).first().user
    chatb = ChatData.objects.get(user=userb, chat=msg.chat)
    rooma = pickle.loads(chata.data)
    roomb = pickle.loads(chatb.data)
    if tip is None:
        rooma.update(algo.UpdateInfo(algo.UpdateType.OUTCOME_MSG,
                                msg.text))
    else:
        rooma.update(algo.UpdateInfo(algo.UpdateType.OUTCOME_TIP_MSG,
                                msg.text, tip))
    roomb.update(algo.UpdateInfo(algo.UpdateType.INCOME_MSG,
                                msg.text))
    chata.data = pickle.dumps(rooma)
    chata.save()
    chatb.data = pickle.dumps(roomb)
    chatb.save()

def delete_tip(chatdata, tip_id):
    data = pickle.loads(chatdata.data)
    data.update(algo.UpdateInfo(
        algo.UpdateType.DELETE_TIP, None, tip_id))
    chatdata.data = pickle.dumps(data)
    chatdata.save()

def process_queue_item(job):
    if job.type == 'fetch':
        download_data(User.objects.get(id=int(job.args)))
    elif job.type == 'start_chat':
        start_chat(Chat.objects.get(id=int(job.args)))
    elif job.type == 'message':
        msg, tip = job.args.split('_')
        if tip == 'None':
            tip = None
        else:
            tip = int(tip)
        new_message(Message.objects.get(id=int(msg)), tip)
    elif job.type == 'delete_tip':
        cd, tip_id = job.args.split('_')
        delete_tip(ChatData.objects.get(id=int(cd)), int(tip_id))
    else:
        raise Exception('Unknown job type ' + job.type)
    job.done = True
    job.save()

def stop_processing():
    STOP = True

def process_queue(cnt=Decimal('Infinity')):
    algo.load_model()
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
