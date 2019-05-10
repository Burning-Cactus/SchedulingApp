from django.shortcuts import render, redirect
from django.views import View
from myApp.models import Terminal
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .forms import InputForm, LoginForm
from .models import USER
from django.core.mail import send_mail
from myApp.NavBar import *

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
        activePermission = request.session['activePermission']
        permissions = request.session['permissions']
        navBar = NavBar()
        nav = navBar.getNavBar(activePermission, permissions)
        return render(request, 'shell/commands.html', {"nav": nav})

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
            userPermissions = []
            for i in user.permission:
                if i.__eq__("1") or i.__eq__("2") or i.__eq__("3") or i.__eq__("4"):
                    userPermissions.append(i)
            request.session['permissions'] = userPermissions
            request.session['activePermission'] = userPermissions[0]
            return HttpResponseRedirect('/commands/')


class Logout(View):
    def get(self, request):
        return render(request, 'shell/logout.html')
    def post(self, request):
        request.session.pop("userid", None)
        request.session.pop("permissions", None)
        request.session.pop("activePermission", None)
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
        ret, bool = terminalInstance.accessData()
        if(bool == False):
            render(request, 'shell/error.html')

        allUsers = ret[0]
        allCourses = ret[1]
        allLabs = ret[2]
        assistantAssignments = ret[3]
        instructorAssignments = ret[4]
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

class Email(View):
    def get(self, request):
        return render(request, 'shell/email.html')

    def post(self, request):
       # terminal = Terminal()
       # subject = request.POST["Subject"]
      #message = request.POST["Message"]

        send_mail("fgu", "hi", 'johnaponte123@gmail.com', ['japonte@uwm.edu'], fail_silently=False, auth_user=None, auth_password=None, connection=None, html_message="hi")

class assignAssistantToLab(View):
    def get(self, request):
        return render(request, 'shell/assignAssistantToLab.html')

    def post(self,request):
        terminalInstance = Terminal()
        labid = request.POST['LabId']
        assistantid = request.POST['AssistantId']
        terminalInstance.assignAssistantToLab(labid,assistantid)
        return render(request, 'shell/commands.html')


class assignAssistantToCourse(View):
    def get(self, request):
        return render(request, 'shell/assignAssistantToCourse.html')

    def post(self, request):
        terminalInstance = Terminal()
        Courseid = request.POST['CourseId']
        assistantid = request.POST['AssistantId']
        terminalInstance.assignAssistantToCourse(Courseid,assistantid)

        return render(request, 'shell/commands.html')

class assignInstructorToCourse(View):
    def get(self, request):
        return render(request, 'shell/assignInstructor.html')
    def post(self, request):
        Terminal().assignInstructorToCourse(request.POST['courseID'], request.POST['instructorID'])
class editContactInfo(View):

  def get(self, request):
    return render(request, 'shell/editContactInfo.html')

  def post(self, request):

        email = request.POST['email']
        contactPhone = request.POST['contactPhone']
        officePhone = request.POST['officePhone']
        extension = request.POST['extension']
        terminalInstance = Terminal()
        id = request.session['userid']
        user = USER.objects.get(id=id)
        terminalInstance.login(user.username, user.password)
        response = terminalInstance.editContactInfo(email,contactPhone, officePhone, extension)
        if response.__eq__("Contact information updated"):
            request.method = 'get'
            return render(request, 'shell/commands.html')
        else:
            return redirect('shell/createAccountError.html')


class viewAssistantAssignments(View):
    def get(self, request):
        aid = request.session['userid']
        self.user = USER.objects.get(id=aid)
        self.user.databaseID = aid
        assistantAssignments = Terminal.viewAssistantAssignments(self)
        return render(request, 'shell/viewAssistantAssignments.html', {"assignments": assistantAssignments})

class EditCourse(View):
    def get(self, request):
        return render(request, 'shell/editCourse.html')
    def post(self, request):
        id = request.POST['courseid']
        name = request.POST['coursename']
        coursenumber = request.POST['coursenumber']
        classnumber = request.POST['classnumber']
        classtime = request.POST['time']
        location = request.POST['location']
        Terminal().editCourse(id, name, coursenumber, classnumber, classtime, location)

class switchPermission(View):
    def get(self, request):
        activePermission = request.session["activePermission"]
        user = USER.objects.get(id=request.session["userid"])
        permissions = []

        if user.permission.__contains__('1'):
            permissions.append('1')
        if user.permission.__contains__('2'):
            permissions.append('2')
        if user.permission.__contains__('3'):
            permissions.append('3')
        if user.permission.__contains__('4'):
            permissions.append('4')

        if activePermission == permissions[0]:
            request.session["activePermission"] = permissions[1]
        if activePermission == permissions[1]:
            request.session["activePermission"] = permissions[0]

        return redirect('/commands/')


class createCourse(View):
    def get(self, request):
        return render(request, 'shell/createCourse.html')

    def post(self, request):
        terminalInstance = Terminal()
        user = USER.objects.get(id=request.session['userid'])
        terminalInstance.login(user.username, user.password)

        ret, bool = terminalInstance.createCourse(request.POST['name'], request.POST['courseNumber'],
                                                  request.POST['classNumber'], request.POST['time'],
                                                  request.POST['location'],)

        if bool is False:
            return render(request, 'shell/error.html', {"message": ret})

        return redirect('/commands/')

