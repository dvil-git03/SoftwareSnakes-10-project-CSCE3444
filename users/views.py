#from genericpath import exists -- Not accessed? - Diego 
#from urllib import request
# (Next time, try to not put stuff that is not called in the script, it's okay it wont break anything, but it makes the code messier) -- Remove when Read.
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from .models import FriendRequest, Friends, Userinfo, Userpass
from django.views.decorators.http import require_POST
from django.contrib import messages


# Create your views here.

def viewRoom(request, urlID):
  if 'userid' not in request.session:
    return redirect('authenticate:login')
  
  targetedUser = get_object_or_404(Userinfo, userid=urlID)

  context = {
    'targetedUser': targetedUser
  }

  return render(request, 'myroom.html', context)

def explore(request):
    if 'userid' not in request.session:
        return redirect('authenticate:login')

    current_user_id = request.session['userid']
    query = request.GET.get('q')

    # FRIENDS
    friend_ids = set(
        Friends.objects.filter(userid_id=current_user_id)
        .values_list('friendid', flat=True)
    )

    # REQUESTS
    sent_requests = set(
        FriendRequest.objects.filter(sender_id=current_user_id)
        .values_list('receiver_id', flat=True)
    )

    # SEARCH RESULTS
    results = []
    if query:
        results = Userinfo.objects.filter(
            username__icontains=query
        ).exclude(userid=current_user_id)

    # ALL USERS (future?? maybe show mutual friends or something??)
    all_users = Userinfo.objects.exclude(userid=current_user_id)

    return render(request, 'explore.html', {
        'query': query,
        'results': results,
        'all_users': all_users,
        'friend_ids': friend_ids,
        'sent_requests': sent_requests
    })


def friends(request):
    if 'userid' not in request.session:
        return redirect('authenticate:login')

    current_user_id = request.session['userid']
    query = request.GET.get('q')

    # FRIEND IDS
    friend_ids = set(
        Friends.objects.filter(userid_id=current_user_id)
        .values_list('friendid', flat=True)
    )

    # FRIEND OBJECTS
    friends_list = Userinfo.objects.filter(userid__in=friend_ids)

    # incoming requests
    incoming_requests = FriendRequest.objects.filter(
        receiver_id=current_user_id
    )

    # outgoing requests
    sent_request_ids = set(
        FriendRequest.objects.filter(sender_id=current_user_id)
        .values_list('receiver_id', flat=True)
    )

    sent_requests = FriendRequest.objects.filter(
    sender_id=current_user_id
  )

    # FRIEND SEARCH
    results = []
    if query:
        results = friends_list.filter(
            username__icontains=query
        )

    return render(request, 'friends.html', {
      'friends': friends_list,
      'incoming_requests': incoming_requests,
      'sent_requests': sent_requests,
      'sent_request_ids': sent_request_ids,
      'friend_ids': friend_ids,
      'results': results,
      'query': query
})

def profile(request):
  if 'userid' not in request.session:
    return redirect('authenticate:login')
  # Replaces a JS script that filled in logged in userinfo, by collecting info from the current session.
  user_data = Userinfo.objects.get(userid=request.session['userid'])
  return render(request, 'profile.html', {'user': user_data})

def updateProfile(request):
  if request.method == "POST":
      # Any userinput that was changed gets captured here
      user = Userinfo.objects.get(userid=request.session.get('userid'))
      emailInput = request.POST.get('email', user.email)
      nameInput = request.POST.get('name', user.name)
      usernameInput = request.POST.get('username', user.username)
      passwordInput = request.POST.get('password')
      collegeInput = request.POST.get('college', user.college)
      usersession = request.session.get('userid', user.userid)
      profilePic = request.FILES.get('profilePic', user.profilePicture)

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

        if profilePic in request.FILES:
          user.profilePicture = request.FILES['profilePic']
          user.save()

        request.session['username'] = usernameInput
        request.session['email'] = emailInput
        request.session['name'] = nameInput
        request.session['college'] = collegeInput
      
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
  return render(request, 'home.html')

@require_POST
def logout(request):
  request.session.flush() # now, you would normally NOT do this, but since we have a custom solution it's fine.
  return redirect('authenticate:login')

@require_POST
def add_friend(request):
    if 'userid' not in request.session:
        return redirect('authenticate:login')

    sender_id = request.session['userid']
    receiver_id = request.POST.get('friend_id')

    if str(sender_id) == str(receiver_id):
        return redirect('users:explore')

    existing = FriendRequest.objects.filter(
      Q(sender_id=sender_id, receiver_id=receiver_id) |
      Q(sender_id=receiver_id, receiver_id=sender_id)
    ).exists()

    if not existing:
        FriendRequest.objects.create(
            sender_id=sender_id,
            receiver_id=receiver_id
        )

        # Only useful on Friends page
        messages.success(request, "Friend request sent.", extra_tags="friends")

    else:
        messages.info(request, "Request already sent.", extra_tags="friends")

    return redirect('users:explore')  # stays explore

@require_POST
def accept_friend_request(request): # This is a new view function to handle accepting friend requests, which was not in the original code but is necessary for the "add_friend" functionality (DEAN)
    if 'userid' not in request.session:
        return redirect('authenticate:login')

    current_user_id = request.session['userid']
    sender_id = request.POST.get('sender_id')

    try:
        req = FriendRequest.objects.get(
            sender_id=sender_id,
            receiver_id=current_user_id
        )

        Friends.objects.create(userid_id=current_user_id, friendid=sender_id)
        Friends.objects.create(userid_id=sender_id, friendid=current_user_id)

        req.delete()

        messages.success(request, "Friend request accepted.", extra_tags="friends")

    except FriendRequest.DoesNotExist:
        messages.error(request, "Request not found.")

    return redirect('users:friends')

@require_POST # This is a new view function to handle removing friends, which was not in the original code but is necessary for the "add_friend" functionality (DEAN)
def remove_friend(request):
    if 'userid' not in request.session:
        return redirect('authenticate:login')

    current_user_id = request.session['userid']
    friend_id = request.POST.get('friend_id')

    Friends.objects.filter(userid_id=current_user_id, friendid=friend_id).delete()
    Friends.objects.filter(userid_id=friend_id, friendid=current_user_id).delete()

    messages.success(request, "Friend removed.", extra_tags="friends")

    return redirect('users:friends')

@require_POST # This is a new view function to handle canceling friend requests, which was not in the original code but is necessary for the "add_friend" functionality (DEAN)
def cancel_friend_request(request):
    if 'userid' not in request.session:
        return redirect('authenticate:login')

    user_id = request.session['userid']
    other_id = request.POST.get("user_id")

    FriendRequest.objects.filter(
        sender_id=user_id,
        receiver_id=other_id
    ).delete()

    FriendRequest.objects.filter(
        sender_id=other_id,
        receiver_id=user_id
    ).delete()

    messages.success(request, "Friend request canceled.", extra_tags="friends")

    return redirect('users:friends')
