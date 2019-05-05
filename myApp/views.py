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


class createAccount(View):

  def get(self, request):
    return render(request, 'shell/createAccount.html')

  def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        permission = request.POST['permission']
        email = request.POST['email']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        contactPhone = request.POST['contactPhone']
        officePhone = request.POST['officePhone']
        extension = request.POST['extension']
        terminalInstance = Terminal()
        id = request.session['userid']
        user = USER.objects.get(id=id)
        terminalInstance.login(user.username, user.password)
        response = terminalInstance.createAccount(permission, username, password, email, firstName, lastName, contactPhone, officePhone, extension)
        if response.__eq__("New user created"):
            request.method = 'get'
            return render(request, 'shell/commands.html')
        else:
            return redirect('shell/createAccountError.html')


class createAccountError(View):

    def get(self, request):
      return render(request, 'shell/createAccountError.html')
    def post(self, request):
      return render(request, 'shell/createAccountError.html')


class editAccount(View):

  def get(self, request):
    return render(request, 'shell/editAccount.html')

  def post(self, request):
    terminalInstance = Terminal()
    id = request.session['editID']
    user = USER.objects.get(id=id)
    terminalInstance.login(user.username, user.password)
    response = terminalInstance.editAccount(id, request.POST['Permission'], request.POST['UserName'],
                                                request.POST['Password'], request.POST['Email'], request.POST['FirstName'],
                                                request.POST['LastName'], request.POST['ContactPhone'], request.POST['OfficePhone'],
                                                request.POST['Extension'])
    if response == "User account updated":
        request.session.pop("editID", None)
        return render(request, ['shell/commands.html'])
    if response == "User does not exist":
        request.session.pop("editID", None)
        return render(request, ['shell/editAccountError.html'])
    else:
        request.session.pop("editID", None)
        return render(request, ['shell/editAccountError.html'])


class editSelect(View):

  def get(self, request):
      return render(request, 'shell/editSelect.html')

  def post(self, request):
      #terminalInstance = Terminal()
      #userinstance = request.session['userid']
      try:
          if USER.objects.get(id=request.POST['userid']):
              request.session['editID'] = request.POST['userid']
              return render(request, 'shell/editAccount.html')
      except USER.DoesNotExist:
          return render(request, 'shell/editAccountError.html')


class commands(View):

    def get(self, request):
      return render(request, 'shell/commands.html')

    def post(self, request):
      return render(request, 'shell/commands.html')


class Login(View):
    def get(self, request):
        return render(request, 'shell/login.html')

    def post(self, request):
        terminalInstance = Terminal()
        username = request.POST['UserName']
        password = request.POST['Password']
        response = terminalInstance.login(username, password)
        if not response.__eq__("Logged in as: " + username):
            return render(request, 'shell/loginError.html', {'res': response})
        else:
            user = USER.objects.get(username=username)
            request.session['userid'] = user.id
            return redirect('/commands/')


class Logout(View):
    def get(self, request):
        return render(request, 'shell/logout.html')
    def post(self, request):
        request.session.pop("userid", None)
        del request.session
        return render(request, 'shell/login.html')


class LoginError(View):
    def get(self, request):
      return render(request, 'shell/loginError.html')
    def post(self, request):
      return render(request, 'shell/loginError.html')


class accessAllData(View):

    def get(self, request):
        terminalInstance = Terminal()
        id = request.session['userid']
        user = USER.objects.get(id=id)
        terminalInstance.login(user.username, user.password)
        allUsers, allCourses, allLabs, assistantAssignments, instructorAssignments = terminalInstance.accessData()
        return render(request, 'shell/accessAllData.html', {"allUsers": allUsers, "allCourses": allCourses, "allLabs": allLabs, "assistantAssignments": assistantAssignments, "instructorAssignments": instructorAssignments})


class deleteSelect(View):
    def post(self, request):
        userid = request.POST["userid"]

        # if the UserID exists
        if USER.objects.filter(databaseID=userid).count() == 1:
            return redirect("/deleteAccount/")

        # else go home
        return render(request, "/commands/")


class deleteAccount(View):
    def get(self, request):
        terminalInstance = Terminal()
        response = terminalInstance.login(username, password)
        userid = request.GET["userid"]  # is this a thing?
        # call model.py's deleteAccount method
        Terminal.deleteAccount(response, userid)
        return render(request, "/commands/")

class deleteCourse(View):
    def post(self, request):
        courseid = request.POST["courseid"]
        terminalInstance = Terminal()
        response = terminalInstance.login(username, password)

        # if the UserID exists
        if USER.objects.filter(databaseID=courseid).count() == 1:
            Terminal.deleteAccount(response, courseid)
            return render(request, "/commands/")

        # else go home
        return render(request, "/commands/")
