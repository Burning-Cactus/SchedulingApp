from django.shortcuts import render
from django.views import View
from myApp.models import Terminal
# Create your views here.
class Driver(View):
  def get(self,request):
    return render(request, 'main/index.html')
  def post(self,request):
    yourInstance = Terminal()
    commandInput = request.POST["command"]
    if commandInput:
      response = Terminal.command(commandInput)
    else:
      response = ""
    return render(request, 'main/index.html',{"message":response})
