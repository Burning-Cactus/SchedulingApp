from django.shortcuts import render,redirect
from django.views import View
from myApp.models import Terminal
from django.http import HttpRequest, HttpResponse
from .forms import InputForm, LoginForm
from .models import USER
# Create your views here.
class Shell(View):
  # Rocks way
  #def get(self,request):
    #return render(request, 'shell/index.html')

  def get(self):
    request = HttpRequest()
    return render(request, 'shell/index.html')
  def post(self,request):
    yourInstance = Terminal()
    commandInput = request.POST["command"]
    if commandInput:
      response = commandInput #Terminal.command(commandInput)
    else:
      response = ""
    return render(request, 'shell/index.html',{"message":response})

  def shellForm(request):
    if request.method == 'POST':
      form = InputForm(request.POST)
      if form.is_valid():

        command = form.cleaned_data['command']
        Terminal.command(command)
        return redirect('shell/')

    form = InputForm()

    return render(request, 'shell/index.html', {'form': form})

  def login(request):
    if request.method == 'POST':
      form = LoginForm(request.POST)
      if form.is_valid():

        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = None
        try:
          user = USER.objects.get(username=username)
        except:
          return HttpResponse("NOT LOGGED IN!!!!!! <a href=http://127.0.0.1:8000>Try Again</a>")


        if(user.password == password):
          return redirect('shell/')


    form = LoginForm()

    return render(request, 'shell/login.html', {'form': form})



