from django.contrib import admin
from .models import Category, Product, Photo, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    prepopulated_fields = {'slug': ('name', )}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['title', 'body']

admin.site.register(Photo)