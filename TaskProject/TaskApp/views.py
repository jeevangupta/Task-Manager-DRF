from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import (Tasks)
from .serializers import (TaskSerializer)

@api_view(['GET','POST'])
def home(request):
    
    data = {
        "demo_id": 123,
        "demo_title": "Demo Title",
        "demo_decsription": "This is demo description",
        "demo_status": "Demo Status"
    }

    if request.method == "GET":
        print("Its GET")
        return Response(data, status=status.HTTP_200_OK)  # Successful GET request


    elif request.method == "POST":
        print("Its a POST method")
        return Response(data, status=status.HTTP_201_CREATED)  # Resource created


    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)  # Method not allowed



class TaskManagerAPI(APIView):
    def get(self, request):
        objs = Tasks.objects.all()
        serializer = TaskSerializer(objs, many = True)

        return Response(serializer.data)
    

    def post(self, request):
        data = request.data
        serializer = TaskSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    #Use patch for partial update
    def patch(self, request):
        data = request.data
        obj = Tasks.objects.get(id = data['id'])
        serializer = TaskSerializer(obj, data = data, partial= True)

        if serializer.is_valid():
            return Response(serializer.data)
        
        return Response(serializer.errors)


    def delete(self, request):
        data = request.data
        obj = Tasks.objects.get(id = data['id'])
        obj.delete()
        
        return Response({'message':'Person deleted'})