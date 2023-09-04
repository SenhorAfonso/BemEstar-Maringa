
from django.contrib.messages import constants
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect

class ValidateAccess:

    def __init__(self, request, email, password, confirm_password, cpf, sus, birthday):
        self.__request = request
        self.__email = email
        self.__password = password
        self.__confirm_password = confirm_password
        self.__cpf = cpf
        self.__sus = sus
        self.__birtday = birthday

    def validateCpf(self):
        #TODO: conectar API para validar cpf
        return True

    def validadeSus(self):
        if self.__sus[0] == 7:
            return True
        messages.add_message(self.__request, constants.ERROR, 'O número do cartão SUS entrado é inválido!')
        return False
    
    def validateBirthday(self):
        from datetime import datetime as dt

        now_date = dt.now()
        now_year = now_date.year

        birthday = self.__birtday.split('-')

        if birthday[0] > now_year:
            messages.add_message(self.__request, constants.WARNING, 'O ano de nascimento é inválido!')
            return False
        return True


    def validate_password(self):
        import re

        if not bool(re.match('([A-Za-z0-9!@#$&*()]+){8,}', self.__password)) and bool(re.match('([A-Za-z0-9!@#$&*()]+){8,}', self.__confirm_password)):
            messages.add_message(self.__request, constants.ERROR, 'A senha entrada é inválida!')
            return False
        elif (self.__confirm_password != self.__password):
            messages.add_message(self.__request, constants.ERROR, 'As senhas não são iguas!')
            return False
        else:
            return True
        

    def validate_email(self):
        import re

        if bool(re.match('[A-Za-z0-9\.\_]+@[gmail|outlook|hotmail]+.com', self.__email)):
            messages.add_message(self.__request, constants.SUCCESS, 'Usuário cadastrado com sucesso!')
            return True
        else:
            messages.add_message(self.__request, constants.ERROR, 'O e-mail é inválido!')
            return False

        
