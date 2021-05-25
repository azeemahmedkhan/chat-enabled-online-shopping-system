from django.shortcuts import render
from .models import Room
from .serializers import RoomSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

@api_view(['GET', 'POST',])
def create_room(request):
    if request.method == 'GET':
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = RoomSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            room = serializer.save()
            data['room_name'] = room.room_name
        else:
            data = serializer.errors
        return Response(data)