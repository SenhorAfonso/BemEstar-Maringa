from django.shortcuts import render
from django.http import HttpResponse

def bemestar(request):
    # return HttpResponse('BemEstar')
    return render(request, 'C:\\Users\\Unicesumar\\Desktop\\BemEstar-Maringa\\bemestar\\templates\\bemestar.html')
