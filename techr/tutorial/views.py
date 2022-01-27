from curses.ascii import RS
from itertools import product
from django import http
from django.shortcuts import render
from django.http import HttpResponse, response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MyProductSerializer,MyRegisterUserSerializer
from .models import MyRegisterUser,Product
from rest_framework.views import APIView





# Create your views here.
@api_view()
def home(request):
    return Response({'status':200, 'message':'tutorial home page'})



class myregisteruserAPI(APIView):
    def get(self, request):
        user_detail=MyRegisterUser.objects.all()
        serializer=MyRegisterUserSerializer(user_detail, many=True)
        return Response({'status':200, 'payload':serializer.data, 'message':'your user data'})
    def post(self, request):
        data=request.data
        serializer=MyRegisterUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':404, 'message':'your data is not valid'})
        serializer.save()
        return Response({'status':200 , 'payload':serializer.data, 'message':'your data is saved '})
    def put(self, request):
        pass
    def patch(self, request):
        pass
  

class myproductAPI(APIView):
    def get(self, request):
        prod_obj=Product.objects.all()
        serializers=MyProductSerializer(prod_obj, many=True)
        return Response({'status':200, 'payload':serializers.data, 'message':'your product detail'})
    def post(self, request):
        data=request.data
        serializer=MyProductSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':403, 'message':'entered data is incorrect'})
        serializer.save()
        return Response ({'status':200, 'payload': serializer.data,'message':'your data saved successfully' })
    def put(self, request):
        pass
    def patch(self, request):
        pass