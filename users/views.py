from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from .models import Userinfo
from django.views.decorators.http import require_POST

# Create your views here.

def myroom(request):
  if 'userid' not in request.session:
    return redirect('authenticate:login')
  template = loader.get_template('myroom.html')
  return HttpResponse(template.render())

def explore(request):
  if 'userid' not in request.session:
    return redirect('authenticate:login')
  template = loader.get_template('explore.html')
  return HttpResponse(template.render())

def friends(request):
  if 'userid' not in request.session:
    return redirect('authenticate:login')
  template = loader.get_template('friends.html')
  return HttpResponse(template.render())

def profile(request):
  if 'userid' not in request.session:
    return redirect('authenticate:login')
  # Replaces a JS script that filled in logged in userinfo, by collecting info from the current session.
  user_data = Userinfo.objects.get(userid=request.session['userid'])
  return render(request, 'profile.html', {'user': user_data})

def settings(request):
  if 'userid' not in request.session:
    return redirect('authenticate:login')
  template = loader.get_template('settings.html')
  return HttpResponse(template.render())

def main(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

@require_POST
def logout(request):
  request.session.flush() # now, you would normally NOT do this, but since we have a custom solution it's fine.
  return redirect('authenticate:login')