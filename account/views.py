from django.shortcuts import render
from .models import CustomUser, Vendor
from .serializers import UserRegistrationSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

@api_view(['POST',])
@permission_classes([AllowAny])
def user_registration(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Successfully Registered.'
            data['username'] = account.username
            data['email'] = account.email
            token = Token.objects.get(user=account).key
            data['token'] = token
            if account.is_vendor == True:
                data['is_vendor'] = True
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(data)
        