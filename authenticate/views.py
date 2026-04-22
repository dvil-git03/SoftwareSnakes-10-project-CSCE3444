from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.db import IntegrityError
from .models import Userinfo, Userpass


# Create your views here.

def login(request):
    if request.method == "POST":
        usernameInput = request.POST.get('username')
        passwordInput = request.POST.get('password')

        if not usernameInput or not passwordInput:
            messages.error(request, "Username and Password are required.")
            return render(request, "log_in.html")
        
        # Exception checking for proper user inputs
        try:
            user = Userinfo.objects.get(username=usernameInput)
            authorizedEntry = Userpass.objects.get(userid=user)

            if check_password(passwordInput, authorizedEntry.password):
                request.session['userid'] = user.userid
                request.session['username'] = user.username
                request.session['email'] = user.email
                request.session['college'] = user.college
                return redirect('users:myroom')
            else:
                messages.error(request, "Invalid Username or Password.") # While this may be checking passwords, we should report a vague message to the user for security.
        except Userinfo.DoesNotExist:
            messages.error(request, "Invalid Username or Password.")
        except Exception as e:
            messages.error(request, f"An unknown error occurred: {e}")
    return render(request, 'log_in.html')

def signup(request):
    if request.method == "POST":
        emailInput = request.POST.get('email')
        nameInput = request.POST.get('name')
        usernameInput = request.POST.get('username')
        passwordInput = request.POST.get('password')

        if not usernameInput or not passwordInput:
            messages.error(request, "Username and Password are required.")
            return render(request, "sign_up.html")
        try:
            # Creating our user for registration using the supplied information from the POST request.
            user = Userinfo(username=usernameInput, email=emailInput, name=nameInput)
            user.save()

            # We are storing a hash of the password in the database as it's not good to store a password in plaintext.
            hashedPassword = make_password(passwordInput)

            # Storing hashed credentials in Userpass.
            userAuthentication = Userpass(userid=user, password=hashedPassword)
            userAuthentication.save()

            return redirect('authenticate:login')
        
        #except IntegrityError:
        #    messages.error(request, "This account already exists.")
        except Exception as e:
            messages.error(request, f"An unknown error occurred: {e}")  
    return render(request, "sign_up.html")