from django.urls import path
from . import views

urlpatterns = [
    path('api/categories/', views.category_list)
]