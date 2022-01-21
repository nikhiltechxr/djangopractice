#created by me
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('hello to main page')

