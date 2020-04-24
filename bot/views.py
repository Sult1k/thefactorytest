from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect


from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from tgmessages.models import tgMessage
from tgmessages.api.serializers import tgSendMessageSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

# API
@api_view(['POST',])
@permission_classes([IsAuthenticated])
def send_tg_message_api(request):

    tg_msge = tgMessage(author_id=request.user)

    if request.method == "POST":
        serializer = tgSendMessageSerializer(tg_msge, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            tbot.send_message(request.user.chat_id, "{}, я получил от тебя сообщение:".format(request.user.username))
            tbot.send_message(request.user.chat_id, "{}".format(request.data['body']))
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# BOT
import telebot

TOKEN = '1041789095:AAEphMsZR_yrJylktdNA8K8OrjGtex8jgZo'
#tbot = telebot.TeleBot(TOKEN)
# Для PythonAnyWhere threaded=False
tbot = telebot.TeleBot(TOKEN, threaded=False)

@csrf_exempt
def bot(request):

    if request.META['CONTENT_TYPE'] == 'application/json':

        json_data = request.body.decode('utf-8')
        update = telebot.types.Update.de_json(json_data)
        tbot.process_new_updates([update])

        return HttpResponse("")

    else:
        raise PermissionDenied

@tbot.message_handler(commands=["start"])
def start_message(message):
    tbot.send_message(message.chat.id, "Привет, я тестовый бот.\nМогу присылать твои сообщения, отправленные по API.\nВсе отправленные мне сообщения в телеграм принимаю как токен")

# GET TOKEN
@tbot.message_handler(content_types=["text"])
def get_okn(message):
    try:
        user = User.objects.get(token=message.text)
        if user.chat_id == None or user.chat_id == '':
            user.chat_id = message.chat.id
            user.save()
            tbot.send_message(message.chat.id, "Welcome!")
        else:
            tbot.send_message(message.chat.id, "Invalid token")
    except:
        tbot.send_message(message.chat.id, "Invalid token")