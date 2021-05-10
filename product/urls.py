from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list),
    path('categories/<slug:slug>/', views.category_detail),
    path('products/', views.product_list),
    path('products/<slug:slug>/', views.product_detail),
    path('comments/', views.comment_list),
    path('photos/', views.photo_list.as_view()),
]