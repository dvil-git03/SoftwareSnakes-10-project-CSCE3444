from django.urls import path
from . import views

urlpatterns = [
    path('users/myroom', views.myroom, name='myroom'),
    path('users/explore', views.explore, name='explore'),
    path('users/friends', views.friends, name='friends'),
    path('users/profile', views.profile, name='profile'),
    path('users/settings', views.settings, name='settings'),
    path('', views.main, name='main')
]