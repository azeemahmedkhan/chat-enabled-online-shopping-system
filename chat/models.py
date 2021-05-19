from django.db import models
from django.contrib.auth import get_user_model

class Room(models.Model):
    user = models.CharField(max_length=250, default='admin')
    vendor = models.CharField(max_length=250, default='admin')
    room_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.room_name

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='room', on_delete=models.CASCADE)
    username = models.CharField(max_length=250)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username + ' | ' + self.message[:30]
