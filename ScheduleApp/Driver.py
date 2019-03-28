from django.shortcuts import render
from django.views import View
from main.models import YourClass
# Create your views here.


class Driver(View):
    
  def get(self,request):
    return render(request, 'main/index.html')
  def post(self,request):
    yourInstance = YourClass()
    commandInput = request.POST["command"]
    if commandInput:
      response = yourInstance.command(commandInput)
    else:
      response = ""
    return render(request, 'main/index.html',{"message":response})