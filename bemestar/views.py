from django.shortcuts import render
from django.http import HttpResponse
from .models import bemestar
from general_utils import DataBaseAccess

import os

def bemestar(request):
    conn = DataBaseAccess().startConnection()
    db = conn['bem_estar_maringa']
    coll = db['bemestar-alimentacao']

    context = {}
    for collection in ['alimentacao', 'exercicios', 'mental']:
        collName = f'bemestar-{collection}'
        coll = db[collName]

        context[collName] = list(coll.find())

    return render(request, 'bemestar.html', context={'bemestardb': context})
