#this is created by me

from django.urls import path
from . import views

urlpatterns=[
    path('', views.learntechhome, name='learntechhome'),
    path("doubtcouter/", views.doubtcounter, name='doubtcouter'),
    path("contactus",views.contact,name='contact'),
    path("yourtutoriallist", views.yourtutoriallist, name='yourtutoriallst'),
    path('account',views.youraccount, name='youraccount')
]