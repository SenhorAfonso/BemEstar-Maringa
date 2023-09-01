from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils import ValidateAccess, DataBaseAcess
from django.contrib.messages import constants
from django.contrib import messages

def homepage(request):

    return render(request, 'homepage.html')

def realizar_cadastro(request):

    if request.method == 'POST':
        client = DataBaseAcess().startConnnection()
        db = client['bem-estar-maringa']
        collection = db['users']

        user_email = request.POST.get('input-email-signup')
        user_password = request.POST.get('input-password-signup')
        user_confirm_password = request.POST.get('input-confirm-password-signup')

        filter = {'email' : user_email}
        if collection.count_documents(filter) > 0:
            messages.add_message(request, constants.WARNING, 'O e-mail entrado já está cadastrado!')
            print('O e-mail entrado já está cadastrado!')
            return redirect('/home')
        
        else:
            user_signin = ValidateAccess(request, user_email, user_password, user_confirm_password)

            if user_signin.validate_email() and user_signin.validate_password():
                
                user = {
                    'email' : user_email,
                    'password' : user_password
                }

                collection.insert_one(user)
                print('usuário cadastrado')
                return redirect('/home')

    client.close()
    return redirect('/home')