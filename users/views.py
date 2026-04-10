from django.shortcuts import render, HttpResponse
from django.template import loader

# Create your views here.

def users(request):
  template = loader.get_template('myroom.html')
  return HttpResponse(template.render())