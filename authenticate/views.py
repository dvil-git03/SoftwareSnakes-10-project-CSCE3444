from django.shortcuts import render, HttpResponse
from django.template import loader


# Create your views here.

def login(request):
    template = loader.get_template('log_in.html')
    return HttpResponse(template.render())

def signup(request):
    template = loader.get_template('sign_up.html')
    return HttpResponse(template.render())