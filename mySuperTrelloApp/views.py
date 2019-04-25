import json
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import *


# Create your views here.
def mainpage(request):
    template = loader.get_template('mySuperTrelloApp/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def get_descs(request):
    """Возвращает данные о досках и карточках в формате JSON"""
    descs = Desc.objects.all()
    descsJson = []
    for desc in descs:
        descJson = {}
        descJson['name'] = desc.name
        cards = [{'text': card.text, 'position': card.position} for card in desc.card_set.all()]
        descJson['cards'] = cards
        descsJson.append(descJson)

    return HttpResponse(json.dumps(descsJson, ensure_ascii=False), content_type='application/json')