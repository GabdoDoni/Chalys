from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate

def pass_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return ""
    else:
        return "User with username or password does not exist"

def register_new_user(request):
    username = request.POST['username']
    user_first_name = request.POST['first_name']
    user_last_name = request.POST['last_name']
    user_pass = request.POST['password']
    user_pas_validate = request.POST['pass2']
    User.objects.create_user(
        username=username,
        first_name=user_first_name,
        last_name=user_last_name,
        password=user_pass
    )

def check_user(request):
    user = User.objects.filter(username=request.POST['username'])
    if request.POST['password'] != request.POST['pass2']:
        return "Your passwords aren't matchning!"
    if len(user)==0:
        register_new_user(request)
        return ""
    else:
        return "User with this login already exist"
