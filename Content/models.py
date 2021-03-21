from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Exam(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    des = models.CharField(max_length=150)
    date_now = models.DateField(auto_now=True)
    question1 = models.CharField(max_length=100)
    question2 = models.CharField(max_length=100)
    question3 = models.CharField(max_length=100)
    answer1 = models.CharField(max_length=50)
    answer2 = models.CharField(max_length=50)
    answer3 = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
