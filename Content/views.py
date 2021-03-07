from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'Content/index.html')

def exams(request):
    return render(request, 'Content/exams.html')