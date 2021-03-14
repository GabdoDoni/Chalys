from django.shortcuts import render, redirect
from . import views_cases
from .models import Exam, Student
# Create your views here.

def home(request):
    context = {
        'active':request.user.is_authenticated
    }
    return render(request, 'Content/home.html', context)

def exams(request):
    return render(request, 'Content/exams.html')

def exam(request):
    # context = views_cases.exam_views(request)
    context = {}
    if request.method =="GET" and 'exam_id' in request.GET:
        return views_cases.check(request)
    elif request.method =="POST":
        return views_cases.exam_ans(request)
    return render(request, 'Content/exam.html', context)

def subjects(request):
    context = views_cases.exam_views(request)
    return render(request, 'Content/subjects.html', context)

def finish_exam_view(request):
    context = views_cases.exam_views(request)
    return render(request, 'Content/succeed.html', context)

def error(request):
    context = views_cases.exam_views(request)
    return render(request, 'Content/error.html', context)

