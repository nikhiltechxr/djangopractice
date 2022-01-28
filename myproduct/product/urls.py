from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views 



urlpatterns = [
    path('productdetail/' , views.ProdcatAPIView.as_view()),
    path('categorydetail/', views.catAPIView.as_view()),
    path('', views.producthome)
]
