from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('room/<int:urlID>', views.viewRoom, name='viewRoom'),
    path('explore', views.explore, name='explore'),
    path('friends', views.friends, name='friends'),
    path('profile', views.profile, name='profile'),
    path('settings', views.settings, name='settings'),
    path('logout', views.logout, name='logout'),
    path('updateProfile', views.updateProfile, name='updateProfile'),
    path('', views.main, name='main')
]