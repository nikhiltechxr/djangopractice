from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render (request, "ironshop/home1.html")

def playlist(request):
    return HttpResponse ("this is playlist")

def yourlist(request):
    return HttpResponse("this is your list")

def contact(request):
    return HttpResponse ("this is contact")

def doubtwindow(request):
    return HttpResponse("this is doubtwindow")

def submition(request):
    return HttpResponse("this is submition")

def account(request):
    return HttpResponse("this is account")