from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path("", views.Shell.shellForm, name='login'),
    path('shell/', views.Shell.shellForm, name='shell'),
]