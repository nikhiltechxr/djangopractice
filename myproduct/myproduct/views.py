from django.shortcuts import render
from django.http import HttpResponse


def myproducthome(request):
    return HttpResponse('<h1>welcome to myproduct site</h1>')