import json
from sys import flags, is_finalizing
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth import get_user_model
from django.http import request
from .models import Room, Message

User = get_user_model()

flag = 0

class ChatConsumer(WebsocketConsumer):

    def fetch_messages(self):
        messages = Message.objects.filter(room=Room.objects.get(room_name=self.room_name))
        for message in messages:
            data = {
                'message': message.message,
                'author': message.username,
                'flag': 1
            }
            self.send_message(data)


    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if text_data_json['flag'] == 0:
            self.fetch_messages()
        else:
            message = text_data_json['message']
            author = text_data_json['author']
            room_name = self.room_name
            room = Room.objects.get(room_name=room_name)
            Message.objects.create(room=room, username=author, message=message)


            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'author': author,
                }
            )


    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        author = event['author']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'author': author
        }))