from django.shortcuts import render,redirect
from django.views import View
from myApp.models import Terminal
from django.http import HttpRequest, HttpResponse
from .forms import InputForm, LoginForm
from .models import USER
# Create your views here.
class Shell(View):
  response = []
  terminalInstance = Terminal()

  def get(self, request):
    return render(request, 'shell/index.html', {"message": None, "user": ""})

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



