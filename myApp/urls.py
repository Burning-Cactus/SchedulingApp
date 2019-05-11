from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path("", views.Login.as_view()),
    path('deleteAccount/', views.deleteAccount.as_view()),
    path('editLab/', views.editLab.as_view()),
    path('createCourse/', views.createCourse.as_view()),
    path('createLab/', views.createLab.as_view()),
    path('createAccount/', views.createAccount.as_view()),
    path('createAccountError/', views.createAccountError.as_view()),
    path('login/', views.Login.as_view()),
    path('loginError/', views.LoginError.as_view()),
    path('commands/', views.commands.as_view()),
    path('admin/', admin.site.urls),
    path('editAccount/', views.editAccount.as_view()),
    path('editSelect/', views.editSelect.as_view()),
    path('deleteAccount/', views.deleteAccount.as_view()),
    path('deleteSelect/', views.deleteSelect.as_view()),
    path('accessAllData/', views.accessAllData.as_view()),
    path('logout/', views.Logout.as_view()),
    path('email/', views.Email.as_view()),
    path('assignAssistantToLab/', views.assignAssistantToLab.as_view()),
    path('assignAssistantToCourse/', views.assignAssistantToCourse.as_view()),
    path('editCourse/', views.EditCourse.as_view()),
    path('switchPermission/', views.switchPermission.as_view()),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)