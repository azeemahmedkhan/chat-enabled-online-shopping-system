from rest_framework import serializers
from .models import Room

def get_group_name(user1, user2):
    return 'chat_{}_{}'.format(*sorted([user1, user2]))

class RoomSerializer(serializers.ModelSerializer):
    user = serializers.CharField()
    vendor = serializers.CharField()
    class Meta:
        model = Room
        fields = ['room_name', 'user', 'vendor', ]
        extra_kwargs = {
            'room_name': {'read_only': True}
        }

    def save(self):
        user = self.validated_data['user']
        vendor = self.validated_data['vendor']
        room_name = get_group_name(user, vendor)
        try:
            room = Room.objects.get(room_name=room_name)
        except:
            room = None
        if room == None:
            room = Room(room_name=room_name, user=user, vendor=vendor)
            room.save()
        return room
