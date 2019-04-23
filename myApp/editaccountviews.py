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
        user.username = request.POST['UserName']
    if request.POST['Password'] != '~':
        user.password = request.POST['Password']
    if request.POST['Permission'] != '~':
        user.email = request.POST['Permission']
    if request.POST['Email'] != '~':
        user.email = request.POST['Email']
    if request.POST['FirstName'] != '~':
        user.firstName = request.POST['FirstName']
    if request.POST['LastName'] != '~':
        user.LastName = request.POST['LastName']
    if request.POST['ContactPhone'] != '~':
        user.contactPhone = request.POST['ContactPhone']
    if request.POST['OfficePhone'] != '~':
        user.officePhone = request.POST['OfficePhone']
    if request.POST['Extension'] != '~':
        user.extension = request.POST['Extension']