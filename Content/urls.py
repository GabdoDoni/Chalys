from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('subjects', views.subjects, name="sub"),
    path('exams', views.exams, name="exams"),
    path('exam', views.exam, name="exam")    
]