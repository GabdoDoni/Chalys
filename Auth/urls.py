from django.urls import path

from . import views

urlpatterns = [
    path('register', views.registraion_views),
    path('login', views.logining_views)
]