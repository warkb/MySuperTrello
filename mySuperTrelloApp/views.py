import json
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import *


# Create your views here.
def mainpage(request):
    template = loader.get_template('mySuperTrelloApp/index.html')

    # делаем Json с досками и карточками из них
    descs = Desc.objects.all()
    descsJson = []
    for desc in descs:
        descJson = {}
        descJson['name'] = desc.name
        cards = [{'text': card.text, 'position': card.position} for card in desc.card_set.all()]
        descJson['cards'] = cards
        descsJson.append(descJson)
    context = {
        'descsJson': json.dumps(descsJson, ensure_ascii=False)
    }
    return HttpResponse(template.render(context, request))
