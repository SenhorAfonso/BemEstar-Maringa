from django.shortcuts import render
from django.http import HttpResponse
from general_utils import DataBaseAccess

# Create your views here.
def chat(request):
    from datetime import datetime as dt

    client = DataBaseAccess().startConnnection()
    db = client['bem_estar_maringa']
    collection = db['chat']

    user_message = request.POST.get('input-chat-user') if request.POST.get('input-chat-user') is not None else ''
    msg = {}
    print(user_message)

    if '1' in user_message:
        
        msg = {
            'hour' : dt.now(),
            'pacient' : '1',
            'doctor' : '2',
            'message' : user_message,
            'type' : 'sent'
        }

    elif '2' in user_message:
        msg = {
            'hour' : dt.now(),
            'pacient' : '1',
            'doctor' : '2',
            'message' : user_message,
            'type' : 'get'
        }

    collection.insert_one(msg)
    all_chat = list(collection.find({'pacient' : '1', 'doctor' : '2'}))
    
    active_chat = {}
    for row in all_chat:
        active_chat[row['hour']] = {row['type'] : row['message']}

    print(active_chat != None)
    return render(request, 'chat.html', context={'active_chat' : active_chat})
