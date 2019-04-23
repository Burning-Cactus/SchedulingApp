from django.shortcuts import render,redirect
from django.views import View
from myApp.models import Terminal
from django.http import HttpRequest, HttpResponse
from .forms import InputForm, LoginForm
from .models import USER
# Create your views here.
class Shell(View):
  response = [""]
  terminalInstance = Terminal()

  def get(self, request):
    return render(request, 'shell/index.html', {"message": Shell.response, "user": ""})

  def post(self, request):
    if request.method == 'POST':
      form = InputForm(request.POST)
      if form.is_valid():

        userInput = form.cleaned_data['command']

        terminalResponse = Shell.terminalInstance.command(userInput)

        if isinstance(terminalResponse, list):
          Shell.response.extend(terminalResponse)
        else:
          Shell.response.append(terminalResponse)

    return render(request, 'shell/index.html', {"message": Shell.response, "user": Shell.terminalInstance.username})



class editAccount(View):

  def get(self, request, UserName):
    edited = USER.objects.get(username=UserName)
    return render(request, edited, 'shell/editAccount.html')

  def post(self, request, user):
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
