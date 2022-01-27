from django.urls import path
from . import views

urlpatterns=[
    path('', views.home),
    path('accounts/', views.myregisteruserAPI.as_view()),
    path('myproduct/', views.myproductAPI.as_view()),

]

