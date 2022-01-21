#this is created by me

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def about(request):
    ana1txt= request.GET.get('text','off')
    print(ana1txt)
    removepun= request.GET.get('analyzer', 'off')
    analysedtext =''
    punc='''!;'",./'''
    param={'text':ana1txt}
    if removepun == 'on':
        for char1 in ana1txt:
            if char1 not in punc:
                analysedtext = analysedtext + char1
        param={'text': analysedtext}
    
    return render(request, 'about.html',param)