from .models import Exam, Student
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

def check(request):
    exam_id = request.GET['exam_id']
    context = {
        'exam': Exam.objects.get(id=exam_id)
    }
    try:
        answer = Student.objects.get(
            user_id=request.user.id,
            exam_id=exam_id
        )
    except Student.DoesNotExist:
        return render(request, 'Content/exam.html', context)
    else:
        return redirect("error")

def exam_views(request):
    context = {
        'active':request.user.is_authenticated,
        'subjects':Exam.objects.all(),
    }
    stud = Student.objects.filter(user_id=request.user.id)
    ans_student = []
    for ans in stud:
        ans_student.append(student.exam.id)
    context['stud'] = ans_student
    return context

def exam_ans(request):
    answer1 = request.POST['answer1']
    answer2 = request.POST['answer2']
    answer3 = request.POST['answer3']
    exam_id = request.POST['exam.id']
    exam = Exam.objects.get(id=exam_id)
    user = user.objects.get(id=request.user.id)
    stu = Student(user_id=user.id, exam_id=exam.id)
    stu.save()
    if answer1 == exam.answer1:
        exam.points = int(exam.points) + 1
    elif answer2 == exam.answer2:
        exam.points = int(exam.points) + 1
    elif answer3 == exam.answer3:
        exam.points = int(exam.points) + 1 
    return redirect("sub")