from django.shortcuts import render,redirect
from django.views import View
from myApp.models import Terminal
from django.http import HttpRequest, HttpResponse
from .forms import InputForm, LoginForm
from .models import USER

class editAccount(View):

  def get(self, request):
    return render(request, 'shell/editAccount.html')

  def post(self, request):
    response = editAccount(request.session['editID'], request.POST['Permission'], request.POST['UserName'],
                request.POST['Password'], request.POST['Email'], request.POST['FirstName'],
                request.POST['LastName'], request.POST['ContactPhone'], request.POST['OfficePhone'],
                request.POST['Extension'])
    if response == "User account updated":
        return render(request, ['http://127.0.0.1:8000/home'])
    if response == "User does not exist":
        return render(request, ['shell/editAccount.html'])
    else:
        return render(request, ['shell/editAccount.html'])



