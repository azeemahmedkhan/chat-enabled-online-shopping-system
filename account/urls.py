from django.urls import path
from .views import user_registration
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'account'

urlpatterns = [
    path('register/', user_registration, name='user_registration'),
    path('login/', obtain_auth_token, name='user_login'),
]