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


class AdminView(View):
  def get(self, request):
    if request.session.get("username", None):
      return redirect("/secpage/")

    return render(request, "homepage.html")

  def post(self, request):
    print(request.POST)
    usn = request.POST["username"]
    pswd = request.POST["password"]

    if USER.objects.filter(username=usn).count() == 0:  # not exist
      USER(username=usn, password=pswd).save()

    if USER.objects.filter(username=usn)[0].password == pswd:
      request.session["username"] = usn
      return redirect("/secpage")

    return render(request, "homepage.html")


class SecondView(View):
  def get(self, request):
    if not request.session.get("username", None):
      return redirect("/admin")

    return render(request, "secondpage.html", {"username": request.session["username"]})


def logout(request):
  request.session.pop("username", None)
  return redirect("/admin")

