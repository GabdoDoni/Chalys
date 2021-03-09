from django.shortcuts import render

from .forms import RegForm
from .views_cases import register_new_user
# Create your views here.


def registraion_views(request):
    context = {
        'forms':RegForm()
    }
    if request.method == "POST":
        register_new_user(request)
    return render(request, 'Auth/registration.html', context)

def logining_views(request):
    return render(request, 'Auth/logining.html')