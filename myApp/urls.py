from django.conf.urls import url
from django.urls import path
from myApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from .views import AdminView, SecondView, logout
urlpatterns = [
    path("", views.Shell.as_view()),
    path('db/', admin.site.urls),
    path('admin/', AdminView.as_view(), name="ad"),
    path('secpage/', SecondView.as_view(), name="sp"),
    path('logout/', logout, name="lo"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)