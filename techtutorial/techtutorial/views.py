#this is created by me 

from django.http import HttpResponse
from django.shortcuts import render

def techtutorialhome(request):
    return render(request, "techtutorialhome.html")