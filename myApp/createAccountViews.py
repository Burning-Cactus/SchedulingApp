from django.shortcuts import render,redirect
from django.views import View
from myApp.models import Terminal
from django.http import HttpRequest, HttpResponse
from myApp.forms import InputForm, LoginForm
from myApp.models import USER

class createAccount(View):

  def get(self, request):
    return render(request, 'shell/createAccount.html')

  def post(self, request):
        username = request.POST['UserName']
        password = request.POST['Password']
        permission = request.POST['Permission']
        email = request.POST['Email']
        firstName = request.POST['FirstName']
        lastName = request.POST['LastName']
        contactPhone = request.POST['ContactPhone']
        officePhone = request.POST['OfficePhone']
        extension = request.POST['Extension']
        response = Terminal.createAccount(permission, username, password, email, firstName, lastName, contactPhone, officePhone, extension)
