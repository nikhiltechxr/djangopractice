from django import http
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view()
def home(request):
    return Response({'status':200, 'message':'tutorial home page'})