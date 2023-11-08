from django.shortcuts import render
from django.http import HttpResponse

def perfil(request):

    return render(request, 'profile.html')