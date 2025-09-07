from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("こんにちは！世界！")

def hobby(request):
    return HttpResponse("私のhobbyは歩くことかもしれません")

def greet(request, name):
    message = "こんにちは" + name + "さん"
    return HttpResponse(message)