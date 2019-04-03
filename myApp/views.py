from django.shortcuts import render,redirect
from django.views import View
from myApp.models import Terminal
from django.http import HttpRequest, HttpResponse
from .forms import InputForm, LoginForm
from .models import USER
# Create your views here.
class Shell(View):

  def get(self, request):
    form = InputForm()
    return render(request, 'shell/index.html', {"form": form})

  def post(self, request):
    if request.method == 'POST':
      form = InputForm(request.POST)
      if form.is_valid():

        userInput = form.cleaned_data['command']
        terminalInstance = Terminal()
        response = terminalInstance.command(userInput)

    form = InputForm()

    return render(request, 'shell/index.html', {'form': form, "message": response})



