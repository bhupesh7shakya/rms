from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import *
from .serializers import *


class CategoryView(APIView):
    def get(self,*args,**kwargs):
        categories = Category.objects.all()
        serializer=CategorySerializer(categories,many=True)
        
        return Response(serializer.data,status=status.HTTP_200_OK)

# Create your views here.
@api_view(['GET','POST'])
def category_list(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer=CategorySerializer(categories,many=True)
        
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        serializer=CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            
        return Response(
            serializer.data
            ,status=status.HTTP_201_CREATED)


@api_view(['GET',"PATCH","DELETE"])        
def category_detail(request,pk):
    category=get_object_or_404(Category,pk=pk)
    if request.method=="GET":
        serializer=CategorySerializer(category)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method=="PATCH":
        
        serializer=CategorySerializer(category,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
            serializer.data
            ,status=status.HTTP_200_OK
            )
            
    if request.method=="DELETE":
        food=Food.objects.filter(category=category)
        if food.count()>0:
            return Response({
                "detail":"You can't delete data Its is protect "
            })
        category.delete()
        return Response(
            {"detail":"Data has been deleted"}
            ,status=status.HTTP_204_NO_CONTENT
            )
    



