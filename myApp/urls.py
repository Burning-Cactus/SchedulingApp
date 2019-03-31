from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path("", views.Shell.login, name='login'),
    path('shell/', views.Shell.shellForm, name='shell'),
]