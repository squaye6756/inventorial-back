# Create your views here.
from rest_framework import generics
from .serializers import UserSerializer
from .models import User

from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
import json

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

def check_login(request):
    if request.method == 'GET':
        return JsonResponse({})
    if request.method == 'PUT':
        jsonRequest = json.loads(request.body) #request -> json format
        username = jsonRequest['username']
        password = jsonRequest['password']
        try:
            if User.objects.get(username=username): #see if username exists in db
                user = User.objects.get(username=username)  #find user object with matching username
                if check_password(password, user.password): #check if passwords match
                    return JsonResponse({'id': user.id, 'username': user.username}) #if passwords match, return a user dict
                else: #passwords don't match
                    return JsonResponse({"error":"Incorrect Password"})
            else: #if username doesn't exist in db, return empty dict
                return JsonResponse({})
        except:
            return JsonResponse({"error":"No Matching Username"})
