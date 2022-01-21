from pickle import TRUE
from django.http import request
#from django.shortcuts import render

from rest_framework.decorators import api_view , renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response

#from apipractice.app1.serializers import mystudentserializer
from .models import *
from .serializers import *
@api_view(['GET'])

# Create your views here.
def home(request):
    stdnt=Student.objects.all()
    serializer=mystudentserializer(stdnt, many=TRUE)
    return Response({'status':'ggg', 'payload':serializer.data})