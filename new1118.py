from funclapi.models import user, wefamily, food, eat
from linebot.models import *
from linebot.models import MessageEvent, TextSendMessage, TextMessage
from .models import user, wefamily, food, eat
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

items = food.objects.filter(kind='飯類', calories__lte=200).items
print (items)