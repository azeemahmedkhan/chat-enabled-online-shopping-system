from . import views
from django.urls import path

urlpatterns = [
    path('create_room/', views.create_room)
]