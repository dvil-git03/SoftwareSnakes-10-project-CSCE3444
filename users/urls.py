from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('room/', views.viewRoom, name='myRoom'),
    path('room/<int:urlID>', views.viewRoom, name='viewRoom'),
    path('explore', views.explore, name='explore'),
    path('friends', views.friends, name='friends'),
    path('profile', views.profile, name='profile'),
    path('settings', views.settings, name='settings'),
    path('logout', views.logout, name='logout'),
    path('updateProfile', views.updateProfile, name='updateProfile'),
    path('', views.main, name='main'),
    path('add_friend', views.add_friend, name='add_friend'),
    path('accept_request', views.accept_friend_request, name='accept_friend_request'),
    path('remove_friend', views.remove_friend, name='remove_friend'),
    path('cancel_request', views.cancel_friend_request, name='cancel_request'),
    path('cancel-friend-request/', views.cancel_friend_request, name='cancel_friend_request')
]
