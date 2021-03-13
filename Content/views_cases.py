from .models import Exam, Student
from django.contrib.auth.models import User



def exam_views(request):
    context = {
        'active':request.user.is_authenticated,
        'subjects':Exam.objects.all()
    }
    return context