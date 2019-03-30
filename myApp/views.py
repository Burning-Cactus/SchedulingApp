from django.shortcuts import render
from django.views import View
from myApp.models import Terminal
# Create your views here.
class Shell(View):
  # Rocks way
  #def get(self,request):
    #return render(request, 'shell/index.html')

  def get(self):
    request = None
    return render(request, 'shell/index.html')
  def post(self,request):
    yourInstance = Terminal()
    commandInput = request.POST["command"]
    if commandInput:
      response = Terminal.command(commandInput)
    else:
      response = ""
    return render(request, 'main/index.html',{"message":response})

  # prints message to the webpage
  def echo(self, request, message):
    return render(request, 'main/index.html', {"":message})