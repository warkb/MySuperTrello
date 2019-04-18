from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .my_bitch_db import *

# Create your views here.
def mainpage(request):
    template = loader.get_template('mySuperTrelloApp/index.html')
    context = {
        'lists': lists
    }
    return HttpResponse(template.render(context, request))
