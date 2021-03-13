from django.shortcuts import render
from . import views_cases
from .models import Exam
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
        exam_id = request.GET['exam_id']
        context = {
            'exam': Exam.objects.get(id=exam_id)
        }
    return render(request, 'Content/exam.html', context)

def subjects(request):
    context = views_cases.exam_views(request)
    return render(request, 'Content/subjects.html', context)