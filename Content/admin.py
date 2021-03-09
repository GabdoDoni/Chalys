from django.contrib import admin

from .models import Student, Exam
# Register your models here.

admin.site.register(Exam)
admin.site.register(Student)

