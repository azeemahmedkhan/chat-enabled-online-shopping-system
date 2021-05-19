from django.contrib import admin
from .models import Room, Message

admin.site.register(Room)

class MessageAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp', )

admin.site.register(Message, MessageAdmin)
