from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('subjects', views.subjects),
    path('exams', views.exams),
    path('exam', views.exam)    
]