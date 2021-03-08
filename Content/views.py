from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'Content/home.html')

def exams(request):
    return render(request, 'Content/exams.html')

def exam(request):
    return render(request, 'Content/exam.html')

def subjects(request):
    return render(request, 'Content/subjects.html')