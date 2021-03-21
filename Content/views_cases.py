from .models import Exam, Student
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

def check(request):
    exam_id = request.GET['exam_id']
    context = {
        'exam': Exam.objects.get(id=exam_id),
        'active':request.user.is_authenticated       
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
        'student':Student.objects.all()
    }
    stud = Student.objects.filter(user_id=request.user.id)
    ans_student = []
    for ans in stud:
        ans_student.append(ans.exam.id)
    context['stud'] = stud
    context['stud1'] = ans_student 
    return context

def exam_ans(request):
    answer1 = request.POST['answer1']
    answer2 = request.POST['answer2']
    answer3 = request.POST['answer3']
    exam_id = request.POST['exam_id']
    exam = Exam.objects.get(id=exam_id)
    user = User.objects.get(id=request.user.id)
    stu = Student(user_id=user.id, exam_id=exam.id)
    if answer1 == exam.answer1 and answer2 == exam.answer2 and answer3 == exam.answer3:
        stu.points = int(stu.points) + 3
    elif answer1 != exam.answer1 and answer2 == exam.answer2 and answer3 == exam.answer3:
        stu.points = int(stu.points) + 2
    elif answer1 == exam.answer1 and answer2 != exam.answer2 and answer3 == exam.answer3:
        stu.points = int(stu.points) + 2
    elif answer1 == exam.answer1 and answer2 == exam.answer2 and answer3 != exam.answer3:
        stu.points = int(stu.points) + 2
    elif answer1 != exam.answer1 and answer2 != exam.answer2 and answer3 == exam.answer3:
        stu.points = int(stu.points) + 1
    elif answer1 != exam.answer1 and answer2 == exam.answer2 and answer3 != exam.answer3:
        stu.points = int(stu.points) + 1
    elif answer1 == exam.answer1 and answer2 != exam.answer2 and answer3 == exam.answer3:
        stu.points = int(stu.points) + 1 
    else:
         exam.points = 0     
    exam.save()
    stu.save()
    return redirect("sub")


def exam_creation(request):
    user = request.user
    title = request.POST['title']
    des = request.POST['des']
    question1 = request.POST['question1']
    question2 = request.POST['question2']
    question3 = request.POST['question3']
    answer1 = request.POST['answer1']
    answer2 = request.POST['answer2']
    answer3 = request.POST['answer3']
    exam =Exam()
    exam.title = title
    exam.des = des
    exam.question1 = question1
    exam.question2 = question2
    exam.question3 = question3
    exam.answer1 = answer1
    exam.answer2 = answer2
    exam.answer3 = answer3
    exam.owner = user
    exam.save()