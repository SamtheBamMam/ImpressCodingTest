from django.views import generic
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import random
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse
from django.shortcuts import render
from django.db.models import F

from chatbot_tutorial.models import ButtonCall


def chat(request):
    context = {}
    return render(request, 'chatbot_tutorial/chatbot.html', context)


def user(request):
    context = {}
    return render(request, 'chatbot_tutorial/user.html', context)


def table(request):
    records = []
    user_records = ButtonCall.objects.all()
    if not user_records:
        button_call_info = {
            "user": '',
            "fat_count": 0,
            "stupid_count": 0,
            "dumb_count": 0
        }
        records.append(button_call_info)
    else:
        for record in user_records:
            button_call_info = {
                "user": record.user,
                "fat_count": record.fat_count,
                "stupid_count": record.stupid_count,
                "dumb_count": record.dumb_count
            }
            records.append(button_call_info)
    context = {"records": records}
    return render(request, 'chatbot_tutorial/table.html', context)


def respond_to_websockets(message):
    jokes = {
        'stupid': ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",
                   """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""],
        'fat': ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",
                """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """],
        'dumb': [
            """Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for extra thick.""",
            """Yo' Mama is so dumb, she locked her keys inside her motorcycle."""]
    }

    result_message = {
        'type': 'text'
    }
    records_exist = ButtonCall.objects.filter(user=message['user'])
    if not records_exist:
        ButtonCall.objects.create(user=message['user'])
    button_obj = ButtonCall.objects.get(user=message['user'])
    if 'fat' in message['text']:
        result_message['text'] = random.choice(jokes['fat'])
        button_obj.fat_count = F('fat_count') + 1
        button_obj.save()

    elif 'stupid' in message['text']:
        result_message['text'] = random.choice(jokes['stupid'])
        button_obj.stupid_count = F('stupid_count') + 1
        button_obj.save()

    elif 'dumb' in message['text']:
        result_message['text'] = random.choice(jokes['dumb'])
        button_obj.dumb_count = F('dumb_count') + 1
        button_obj.save()

    elif message['text'] in ['hi', 'hey', 'hello']:
        result_message[
            'text'] = "Hello to you too! If you're interested in yo mama jokes, just tell me fat, stupid or dumb and i'll tell you an appropriate joke."
    else:
        result_message[
            'text'] = "I don't know any responses for that. If you're interested in yo mama jokes tell me fat, stupid or dumb."

    return result_message
