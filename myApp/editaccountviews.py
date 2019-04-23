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
    if request.POST['UserName'] != '~':
        USER.username = request.POST['UserName']
    if request.POST['Password'] != '~':
        USER.password = request.POST['Password']
    if request.POST['Permission'] != '~':
        USER.email = request.POST['Permission']
    if request.POST['Email'] != '~':
        USER.email = request.POST['Email']
    if request.POST['FirstName'] != '~':
        USER.firstName = request.POST['FirstName']
    if request.POST['LastName'] != '~':
        USER.LastName = request.POST['LastName']
    if request.POST['ContactPhone'] != '~':
        USER.contactPhone = request.POST['ContactPhone']
    if request.POST['OfficePhone'] != '~':
        USER.officePhone = request.POST['OfficePhone']
    if request.POST['Extension'] != '~':
        USER.extension = request.POST['Extension']
