from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = {
    url(r'^$', views.Shell.get, name='shell'),
    path("", views.Shell.as_view()),
}