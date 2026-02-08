import json

from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CategorySerializer,ProductSerializer
from .models import Category,Product

# Create your views here.
class CategoryCreateView(APIView):
    def post(self,request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Category added successfully'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def get(self,request,pk):
            category_detail = Category.objects.get(id=pk)
            serializer = CategorySerializer(category_detail)
            return JsonResponse({"category-detail":serializer.data},status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            cate = Category.objects.get(id=pk)
            cate.name = request.data['name']
            cate.description = request.data['description']
            return Response({"message":"Category update successfully"},status=status.HTTP_200_OK)
        
    def delete(self,request,pk):
         category_delete = Category.objects.get(id=pk)
         category_delete.delete()
         return Response({'message':"Category Delete successfully"},status=status.HTTP_204_NO_CONTENT)

class ProductView(APIView):
     
     def get(self,request,pk):
            data = Product.objects.filter(category=pk)
            serializer = ProductSerializer(data,many=True)
            return JsonResponse({"product":serializer.data},status=status.HTTP_200_OK)
     
# phone -> ipone,test,iqoo