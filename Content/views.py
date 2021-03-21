from django.shortcuts import render, redirect
from . import views_cases
from .models import Exam, Student
from .forms import ExamCreateForm
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    context = {
        'active':request.user.is_authenticated
    }
    return render(request, 'Content/home.html', context)

def exams(request):
    context = {
        'active':request.user.is_authenticated
    }
    return render(request, 'Content/exams.html', context)

def exam(request):
    context = {
        'active':request.user.is_authenticated
    }
    if request.method =="GET" and 'exam_id' in request.GET:
        return views_cases.check(request)
    elif request.method =="POST":
        return views_cases.exam_ans(request)
    return render(request, 'Content/exam.html', context)

def subjects(request):
    context = views_cases.exam_views(request)
    if request.method == "POST":
        exam_id = request.POST['exam_id']
        exam = Exam.objects.get(id=exam_id)
        exam.delete()
        return redirect('delete')
    return render(request, 'Content/subjects.html', context)

def finish_exam_view(request):
    context = {
        'active':request.user.is_authenticated
    }
    return render(request, 'Content/succeed.html', context)

def error(request):
    context = {
        'active':request.user.is_authenticated
    }
    return render(request, 'Content/error.html', context)

def exam_creation_form(request):
    context = {
        'form':ExamCreateForm(),
        'active':request.user.is_authenticated
    }
    if request.method =="POST":
        views_cases.exam_creation(request)
    return render(request, 'Content/exam_creation.html', context)


def second_exam(request):
    context = {
        'active':request.user.is_authenticated
    }
    return render(request, 'Content/error.html', context)


def delete(request):
    context = {
        'active':request.user.is_authenticated
    }
    return render(request, 'Content/delete.html', context)