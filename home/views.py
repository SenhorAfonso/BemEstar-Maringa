from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils import ValidateAcess

def homepage(request):

    return render(request, 'homepage.html')

def realizar_cadastro(request):

    if request.method == 'POST':

        user_email = request.POST.get('input-email-signup')
        user_password = request.POST.get('input-email-signup')
        user_confirm_password = request.POST.get('input-email-signup')

        #TODO: verificar se o e-mail já não esta cadastrado

        user_sign = ValidateAcess(request, user_email, user_password, user_confirm_password)

        if user_sign.validate_email() and user_sign.validate_password:
            #TODO: abre conexão com o banco e cadastra o usuário
            pass


    return redirect('/home')