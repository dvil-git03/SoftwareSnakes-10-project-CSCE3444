from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Userinfo)
admin.site.register(Userpass)
admin.site.register(Userroom)
admin.site.register(Friends)
admin.site.register(FriendRequest)