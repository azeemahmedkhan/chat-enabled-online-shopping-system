from django.shortcuts import render
from .models import CustomUser, Vendor
from .serializers import UserRegistrationSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST',])
def user_registration(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Successfully Registered.'
            data['username'] = account.username
            data['email'] = account.email
        else:
            data = serializer.errors
        return Response(data)
