from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view()
def home(request):
    return Response ({'status':200, 'message':'success'})

def loginpage(request):
    return render(request, "firstapp/loginpage.html")
