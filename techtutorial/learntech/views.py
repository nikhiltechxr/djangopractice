from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response

@api_view()
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))

# Create your views here.

def learntechhome(request):
    return render(request, 'learntech/learntechhome.html')

def doubtcounter(request):
    return render(request, 'learntech/learntechdoubtcounter.html')

def contact(request):
    return render(request, 'learntech/learntechcontact.html')

def yourtutoriallist(request):
    [...]
    return Response ({'status':"completed", 'name':'AR-VR'}) 

def youraccount(request):
    return render(request, 'learntech/learntechmyaccount.html')