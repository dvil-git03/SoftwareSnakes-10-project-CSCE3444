from django.shortcuts import render, HttpResponse
from django.template import loader

# Create your views here.

def myroom(request):
  template = loader.get_template('myroom.html')
  return HttpResponse(template.render())

def explore(request):
  template = loader.get_template('explore.html')
  return HttpResponse(template.render())

def friends(request):
  template = loader.get_template('friends.html')
  return HttpResponse(template.render())

def profile(request):
  template = loader.get_template('profile.html')
  return HttpResponse(template.render())

def settings(request):
  template = loader.get_template('settings.html')
  return HttpResponse(template.render())

def main(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())