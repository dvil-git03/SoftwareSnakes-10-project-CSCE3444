"""
URL configuration for mydigiroom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from users import views as user_views
from django.views.generic.base import RedirectView

# Dirty trick, but this is honestly so cool I don't even mind it.
favicon_view = RedirectView.as_view(url='/static/images/favicon.ico', permanent=True)

urlpatterns = [
    # Basically, this is a auto-permanent redirect (HTTP 302) that gives an favicon without a base.html.
    re_path(r'^favicon\.ico$', favicon_view),
    path('admin/', admin.site.urls),
    path('', user_views.main, name="main"), # this is pretty hacky, but only way i could get this to properly working without modifying EVERY file again
    path('users/', include('users.urls', namespace='users')),
    path('authenticate/', include('authenticate.urls', namespace='authenticate'))
]

# This is a DEBUG flag, but for now it'll do fine.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)