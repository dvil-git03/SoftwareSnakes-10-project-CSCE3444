from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from .models import Userinfo, Userpass
from django.views.decorators.http import require_POST
from django.contrib import messages

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

def updateProfile(request):
  if request.method == "POST":
      # Any userinput that was changed gets captured here
      emailInput = request.POST.get('email')
      nameInput = request.POST.get('name')
      usernameInput = request.POST.get('username')
      passwordInput = request.POST.get('password')
      collegeInput = request.POST.get('college')
      usersession = request.session.get('userid')
      profilePic = request.FILES.get('profilePic')

      # A Python classic, basically, this is checking if there is ALREADY an existing email or username. 
      # Q stands for Query and using the logical OR (|) to check if either condition is true, EXCLUDING our own.
      conflictExists = Userinfo.objects.filter(Q(email=emailInput) | Q(username=usernameInput)).exclude(userid=usersession).exists()
      if conflictExists: # Oops.
        messages.error(request, f"This email or username already exists.")
        erroredUser = {
          'username': usernameInput,
          'email': emailInput,
          'name': nameInput,
          'college': collegeInput
        }
        return render(request, 'profile.html', {"user": erroredUser})
      
      # Now, time to update this database, putting this in a try/except block because things MAY go wrong.
      try:
        # ONLY manipulating this current users information.
        user = Userinfo.objects.get(userid=usersession)
        user.username = usernameInput
        user.email = emailInput
        user.name = nameInput
        user.college = collegeInput
        user.save()
      
        # If they chose to update their password, we need to rehash it and store it in Userpass.
        if passwordInput:
          userPassword = Userpass.objects.get(userid=usersession)
          userPassword.password = make_password(passwordInput)
          userPassword.save()
          # Updating their session in Realtime, kinda.

        if profilePic:
          user.profilePicture = request.FILES['profilePic']
          user.save()

        request.session['username'] = usernameInput
        
      
      # A error happened, oh no! Please tell Diego :( !
      except Exception as e:
        messages.error(request, f"An unknown error occurred: {e}")
        erroredUser = {
          'username': usernameInput,
          'email': emailInput,
          'name': nameInput,
          'college': collegeInput
        }
        return render(request, 'profile.html', {"user": erroredUser})

      messages.success(request, "Successfully updated profile!")
      return redirect('users:profile')


def settings(request):
  if 'userid' not in request.session:
    return redirect('authenticate:login')
  return render(request, 'settings.html')

def main(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

@require_POST
def logout(request):
  request.session.flush() # now, you would normally NOT do this, but since we have a custom solution it's fine.
  return redirect('authenticate:login')