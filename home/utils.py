
from django.contrib.messages import constants
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect

from abc import ABC, abstractclassmethod

class ValidateAccess:

    def __init__(self, request, email, password, confirm_password, cpf, sus, birthday):
        self.__request = request
        self.__email = email
        self.__password = password
        self.__confirm_password = confirm_password
        self.__cpf = cpf
        self.__sus = sus
        self.__birtday = birthday

    def validate_cpf(self):
        from validate_docbr import CPF

        return CPF().validate(self.__cpf)

    def validade_sus(self):
        if self.__sus[0] == 7:
            return True
        messages.add_message(self.__request, constants.ERROR, 'O número do cartão SUS entrado é inválido!')
        return False
    
    def validate_birthday(self):
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

class Person(ABC):

    def __init__(self, name, cpf, sex, birthdate):
        self.__name = name
        self.__cpf = cpf
        self.__sex = sex
        self.__birthdate = birthdate

    def get_name(self):
        return self.__name

    def get_cpf(self):
        return self.__cpf

    def get_sex(self):
        return self.__sex

    def get_birthdate(self):
        return self.__birthdate
    
class Patient(Person):

    def __init__(self, name, email, password, cpf, sus, sex, birthdate):
        super().__init__(name, cpf, sex, birthdate)
        self.__email = email
        self.__password = password
        self.__sus = sus
    
    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password
    
    def get_sus(self):
        return self.__sus

class Doctor(Person):

    def __init__(self, name, email, password, cpf, sus, sex, birthdate, crm):
        super().__init__(name, cpf, sex, birthdate)
        self.__email = email
        self.__password = password
        self.__sus = sus
        self.__crm = crm