from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils import ValidateAccess
from general_utils import DataBaseAccess
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth.models import User

def homepage(request): 

    return render(request, 'homepage.html')

def realizar_cadastro(request):
    if request.method == 'POST':
        client = DataBaseAccess().startConnnection()
        db = client['bem_estar_maringa']
        collection = db['users']

        user_name = request.POST.get('input-name-signup')
        user_email = request.POST.get('input-email-signup')
        user_password = request.POST.get('input-password-signup')
        user_confirm_password = request.POST.get('input-confirm-password-signup')
        user_cpf = request.POST.get('input-cpf-signup')
        user_sus = request.POST.get('input-sus-card-signup')
        user_sex_f = request.POST.get('input-sex-f-signup')
        user_sex_m = request.POST.get('input-sex-m-signup')
        user_bithdate = request.POST.get('input-date-signup')

        #TODO: tratar os dados de entrada usando javascript e enviar as respostas para o python via API

        if user_sex_f == 'on':
            user_sex = 'F'
        elif user_sex_m == 'on':
            user_sex = 'M'
        else:
            user_sex = 'O'

        if collection.count_documents({'email' : user_email}) > 0:
            messages.add_message(request, constants.WARNING, 'O e-mail entrado já está cadastrado!')
            print('O e-mail entrado já está cadastrado!')
            return redirect('/home')

        elif collection.count_documents({'cpf' : user_cpf}) > 0:
            messages.add_message(request, constants.WARNING, 'O CPF entrado já está cadastrado!')
            print('O CPF já está cadastrado')
            return redirect('/home')
        
        elif collection.count_documents({'cartao-sus' : user_sus}) > 0:
            messages.add_message(request, constants.WARNING, 'O cartão SUS entrado já está cadastrado!')
            print('cartão sus')
            return redirect('/home')
        
        else:
            user_signin = ValidateAccess(request, user_email, user_password, user_confirm_password, user_cpf, user_sus, user_bithdate)

            if user_signin.validate_email() and user_signin.validate_password():
                
                if User.objects.filter(username = user_name).first():
                    messages.add_message(request, constants.WARNING, 'O nome entrado já está cadastrado!')
                    print('nome já cadastrado')
                    return redirect('/home')
                else:
                    user = {
                        'name' : user_name,
                        'email' : user_email,
                        'password' : user_password,
                        'cpf' : user_cpf,
                        'sus_card' : user_sus,
                        'sex' : user_sex,
                        'birthday' : user_bithdate
                    }

                    collection.insert_one(user)
                    
                    user = User.objects.create_user(user_name,
                                                   user_email, 
                                                   user_password).save()

                    print('usuário cadastrado')
                    return redirect('/home')
            else:
                print('dados invalidos')

    client.close()
    return redirect('/home')

def realizar_login(request):
    pass




