from django.urls import path

from . import views

urlpatterns = [
    path('register', views.registraion_views, name="reg"),
    path('login', views.logining_views, name="auth"),
    path('logout', views.logging_out, name="lout")
]