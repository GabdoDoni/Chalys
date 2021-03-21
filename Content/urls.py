from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('subjects', views.subjects, name="sub"),
    path('exams', views.exams, name="exams"),
    path('exam', views.exam, name="exam"),
    path('finish-exam', views.finish_exam_view, name="success"),
    path('error', views.error, name="error"),
    path('exam_creation', views.exam_creation_form, name="examcreat"), 
    path('delete', views.delete, name="delete")    
]