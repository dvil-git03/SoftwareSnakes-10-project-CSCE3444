from django.urls import path
from . import views

urlpatterns = [
    path('authenticate/login', views.login, name='login'),
    path('authenticate/signup', views.signup, name='signup')
]