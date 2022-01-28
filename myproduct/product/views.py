from ast import Pass
from itertools import product
from django import http
from django.shortcuts import render
from uritemplate import partial
from .serializers import ProductTableSerializer, CategoryTableSerializer
from .models import ProductTable, CategoryTable
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response




# Create your views here.

def producthome(request):
    return http.HttpResponse('welcomr to product page')

class ProdcatAPIView(APIView):
    def get(self, request):
        productsobj=ProductTable.objects.all()
        serializer=ProductTableSerializer(productsobj, many=True)
        return Response({'status':200, 'payloads':serializer.data ,"message":'hello you got data'})
        
    def post(self, request):
        data=request.data
        serializer=ProductTableSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"status":403, 'message':'data is not valid'})
        serializer.save()
        return Response({'status':200, 'payload':serializer.data, 'message':'your uploaded data'})

    def put(self, request):
        data=request.data
        #id=request.GET.get('id')
        pro=ProductTable.objects.get(id=request.data['id'])
        serializer=ProductTableSerializer(pro, data=request.data)
        if not serializer.is_valid():
            return Response({"status":403, 'message':'data is not valid'})
        serializer.save()
        return Response({'status':200, 'payload':serializer.data, 'message':'your uploaded data'})

    def patch(self, request):
        data=request.data
        #id=request.GET.get('id')
        #id=request.data['id']
        pro=ProductTable.objects.get(id=request.data['id'])
        serializer=ProductTableSerializer(pro, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({"status":403, 'message':'data is not valid'})
        serializer.save()
        return Response({'status':200, 'payload':serializer.data, 'message':'your uploaded data'})

    def delete(self, request):
        #id=request.GET.get('id')
        pro=ProductTable.objects.get(id=request.data['id'])
        pro.delete()
        return Response({'status':200, 'message':'data deleted'})



class catAPIView(APIView):
    def get(self, request):
        productsobj=CategoryTable.objects.all()
        serializer=CategoryTableSerializer(productsobj, many=True)
        return Response({'status':200, 'payloads':serializer.data ,"message":'hello you got data'})
    def post(self, request):
        data=request.data
        serializer=CategoryTableSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"status":403, 'message':'data is not valid'})
        serializer.save()
        return Response({'status':200, 'payload':serializer.data, 'message':'your uploaded data'})
    def put(self, request):
        pass
    def patch(self, request):
        pass
    def delete(self, request):
        pass
