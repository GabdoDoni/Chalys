from django.shortcuts import render, redirect
from .forms import RegForm, LogForm
from . import views_cases   
from django.contrib.auth import logout
# Create your views here.

def logging_out(request):
    logout(request)
    return redirect("home")

def registraion_views(request):
    context = {
        'forms':RegForm(),
        'error':''
    }
    if request.method == "POST":
        context['error'] = views_cases.check_user(request)
        if context['error'] == '':
            return redirect("auth")
    return render(request, 'Auth/registration.html', context)

def logining_views(request):
    context = {
        'forms':LogForm(),
        'error':''
    }
    if request.method == "POST":
        context['error'] = views_cases.pass_user(request)
        if context['error'] == "":
            return redirect("home")
    return render(request, 'Auth/logining.html', context)