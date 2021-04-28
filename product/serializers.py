from rest_framework import serializers
from .models import Category, Product, Photo, Comment



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']