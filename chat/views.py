from django.shortcuts import render
from django.http import HttpResponse
from general_utils import DataBaseAccess
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from general_utils import DataBaseAccess

@login_required(login_url='/home/realizar_login')
def chat(request):
    from datetime import datetime as dt

    client = DataBaseAccess().startConnnection()
    db = client['bem_estar_maringa']
    collection = db['chat']

    user_message = request.POST.get('input-chat-user') if request.POST.get('input-chat-user') is not None else ''

    msg = {
        'user' : str(request.user),
        'message' : user_message
    }

    collection.insert_one(msg)

    all_chat = list(collection.find())

    print(all_chat)

    return render(request, 'chat.html', context={'chat' : all_chat})
