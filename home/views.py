from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseServerError
from .utils import ValidateAccess, Patient
from general_utils import DataBaseAccess
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def homepage(request):
    return render(request, 'homepage.html')


def realizar_cadastro(request):
    if request.method == 'POST':

        client = DataBaseAccess().startConnection()

        if (isinstance(client, int)):
            return HttpResponseServerError()

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
        isDoctor = request.POST.get('input-isdoctor-signup')
        isNotDoctor = request.POST.get('input-isnotdoctor-signup')

        # TODO: colocar no HTML um botão para diferenciar cadastro de médico do cadastro de paciente
        # TODO: tratar os dados de entrada usando javascript e enviar as respostas para o python via API

        userIsDoctor = True if isDoctor == 'on' else False

        if user_sex_f == 'on':
            user_sex = 'F'
        elif user_sex_m == 'on':
            user_sex = 'M'
        else:
            user_sex = 'O'

        if len(user_name.split(' ')) == 1:
            messages.add_message(request, constants.ERROR, 'Insira seu nome completo!')
            return redirect('/home')

        users_list = [dict(x) for x in collection.find()]

        for user_info in users_list:
            for key, value in user_info.items():
                if value == user_email:
                    messages.add_message(request, constants.WARNING, 'O e-mail entrado já está cadastrado!')
                    return redirect('/home')

                if value == user_cpf:
                    messages.add_message(request, constants.WARNING, 'O CPF entrado já está cadastrado!')
                    return redirect('/home')

                if value == user_sus:
                    messages.add_message(request, constants.WARNING, 'O cartão SUS entrado já está cadastrado!')
                    return redirect('/home')

        # elif collection.count_documents({'email' : user_email}) > 0:
        #     messages.add_message(request, constants.WARNING, 'O e-mail entrado já está cadastrado!')
        #     print('O e-mail entrado já está cadastrado!')
        #     return redirect('/home')
        #
        #
        # elif collection.count_documents({'cpf' : user_cpf}) > 0:
        #     messages.add_message(request, constants.WARNING, 'O CPF entrado já está cadastrado!')
        #     print('O CPF já está cadastrado')
        #     return redirect('/home')
        #
        # elif collection.count_documents({'cartao-sus' : user_sus}) > 0:
        #     messages.add_message(request, constants.WARNING, 'O cartão SUS entrado já está cadastrado!')
        #     print('cartão sus')
        #     return redirect('/home')

        else:
            user_signin = ValidateAccess(request, user_email, user_password, user_confirm_password, user_cpf, user_sus,
                                         user_bithdate)

            if user_signin.validate_email() and user_signin.validate_password():

                if User.objects.filter(username=user_name).first():
                    messages.add_message(request, constants.WARNING, 'O nome entrado já está cadastrado!')
                    print('nome já cadastrado')
                    return redirect('/home')
                else:

                    user = Patient(name=user_name,
                                   email=user_email,
                                   password=user_password,
                                   cpf=user_cpf,
                                   sus=user_sus,
                                   sex=user_sex,
                                   birthdate=user_bithdate)

                    user_data = {
                        'name': user.get_name(),
                        'email': user.get_email(),
                        'password': user.get_password(),
                        'cpf': user.get_cpf(),
                        'sus_card': user.get_sus(),
                        'sex': user.get_sex(),
                        'birthday': user.get_birthdate(),
                        'isDoctor': userIsDoctor
                    }

                    collection.insert_one(user_data)

                    user_data = User.objects.create_user(user.get_name(),
                                                         user.get_email(),
                                                         user.get_password()).save()

                    print('usuário cadastrado')
                    return redirect('/home')
            else:
                print('dados invalidos')

        client.close()
    return redirect('/home')


def realizar_login(request):
    if request.method == 'GET':
        return redirect('/home')

    elif request.method == 'POST':

        login_input = request.POST.get('input-email-cpf-sus-login')
        password_input = request.POST.get('input-password-login')

        user = authenticate(username=login_input, password=password_input)

        if user:
            login(request, user)
            return redirect('/chat')
        return HttpResponse('não autenticado')
