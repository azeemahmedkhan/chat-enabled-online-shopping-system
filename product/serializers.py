from rest_framework import serializers
from .models import Category, Product, Photo, Comment
from account.serializers import UserRegistrationSerializer
from django.conf import settings

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    vendor = UserRegistrationSerializer(read_only=True)
    vendor_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Product
        fields = ['id', 'category_id', 'category', 'name', 'slug', 'vendor', 'vendor_id', 'price', 'description']

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True)
    user = UserRegistrationSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'product', 'product_id', 'user', 'user_id', 'title', 'body']

class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Photo
        fields = ['id', 'photo', 'product_id', 'product']