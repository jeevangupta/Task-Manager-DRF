
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            objs = Tasks.objects.all()
            serializer = TaskSerializer(objs, many = True)

            if serializer.data:
                return Response(serializer.data)
            else:
                return Response({'message':'No Task Found'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:

            return Response({'message':f'Something went Wrong : {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

    def post(self, request):
        data = request.data
        serializer = TaskSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    #Use patch for partial update
    def patch(self, request):
        data = request.data
        try:
            task = Tasks.objects.get(id = data['id'])
        except Tasks.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TaskSerializer(task)
        data["title"] = serializer.data["title"]
        serializer = TaskSerializer(task, data = data, partial= True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        # else:
        #     return Response({'message':'No task found! Invalid task id'}, status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request):
        try:
            data = request.data
            #obj = Tasks.objects.get(id = data['id'])
            obj = Tasks.objects.filter(id = data['id']).first()
            if obj:
                serializer = TaskSerializer(obj)
                obj.delete()
                return Response({'message':f'Task {serializer.data["title"]} deleted'}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({'message':'No task found! Invalid task id'}, status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            return Response({'message':f'Something went Wrong : {e}'}, status=status.HTTP_400_BAD_REQUEST)
    
    
