from django.shortcuts import render

# Create your views here.


def registraion_views(request):
    return render(request, 'Auth/registration.html')

def logining_views(request):
    return render(request, 'Auth/logining.html')