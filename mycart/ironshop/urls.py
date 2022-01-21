#created by me
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="ironshophome"),
    path("playlist/", views.playlist, name="playlists"),
    path("yourlist/", views.yourlist, name="yourlists"),
    path("contact/", views.contact,name="contact"),
    path("doubtwindow/",views.doubtwindow, name="doubtwindow"),
    path("account/",views.account,name="account"),
    path("submition/", views.submition, name="submition")
    
]
