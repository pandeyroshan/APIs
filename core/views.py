from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from .models import dataSet
from django.core import serializers

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def register(request):
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")
    user = User.objects.create_user(username, email, password)
    print(user)
    return Response({'message':'User Registered'},status=HTTP_200_OK)

@csrf_exempt
@api_view(["GET"])
def getData(request):
    data = dataSet.objects.all()
    json_data = serializers.serialize('json', data)
    return Response(json_data, status=HTTP_200_OK)

@csrf_exempt
@api_view(["POST"])
def postData(request):
    topic = request.data.get('topic')
    text = request.data.get('text')
    obj = dataSet.objects.create(topic=topic,text=text)
    obj.save()
    return Response({'message':'Data Saved'},status=HTTP_200_OK)