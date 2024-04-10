
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer

@api_view(['POST'])
def register_view(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()

        token = Token.objects.create(user=user)

        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)

    user = get_object_or_404(User, username=request.data['username'])

    if not user.check_password(request.data['password']):
        return Response("Invalid Password!", status=status.HTTP_404_NOT_FOUND)
    
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)

    return Response({'token': token.key, 'user': serializer.data})


@api_view(['POST'])
def logout_view(request):
    request.user.auth_token.delete()

    return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response({'message': 'Passed'}, status=status.HTTP_200_OK)
