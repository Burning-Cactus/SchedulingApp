from django.shortcuts import render, redirect
from django.views import View
from myApp.models import Terminal
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .forms import InputForm, LoginForm
from .models import USER, LAB_SECTION, A_LIST, I_LIST, COURSE
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
        ret, success = terminalInstance.createAccount(permission, username, password, email, firstName, lastName, contactPhone, officePhone, extension)
        if success is True:
            request.method = 'get'
            return redirect('/commands/')
        else:
            return render(request, '/error/', {"message": ret})


class createAccountError(View):

    def get(self, request):
      return render(request, 'shell/createAccountError.html')
    def post(self, request):
      return render(request, 'shell/createAccountError.html')


class editAccount(View):

  def get(self, request):
    editid = request.session['editID']
    return render(request, 'shell/editAccount.html', {'editID': editid})

  def post(self, request):
    terminalInstance = Terminal()
    editid = request.session['editID']
    user = USER.objects.get(id=editid)
    terminalInstance.login(user.username, user.password)
    response, success = terminalInstance.editAccount(editid, request.POST['Permission'], request.POST['UserName'],
                                                     request.POST['Password'], request.POST['Email'],
                                                     request.POST['FirstName'],
                                                     request.POST['LastName'], request.POST['ContactPhone'],
                                                     request.POST['OfficePhone'],
                                                     request.POST['Extension'])
    if success is True:
        request.session.pop("editID", None)
        return render(request, ['shell/commands.html'])
    if success is False:
        request.session.pop("editID", None)
        return render(request, ['shell/editAccountError.html'])


class editSelect(View):

  def get(self, request):
      terminalInstance = Terminal()
      id = request.session['userid']
      user = USER.objects.get(id=id)
      terminalInstance.login(user.username, user.password)
      ret, bool = terminalInstance.accessData()
      if (bool == False):
          render(request, 'shell/error.html')

      allUsers = ret[0]
      return render(request, 'shell/editSelect.html', {'allUsers': allUsers})

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
        userTitle = ""

        if int(activePermission) is 1:
            userTitle = "Supervisor"
        if int(activePermission) is 2:
            userTitle = "Administrator"
        if int(activePermission) is 3:
            userTitle = "Instructor"
        if int(activePermission) is 4:
            userTitle = "Assistant"
        return render(request, 'shell/commands.html', {"nav": nav, "userTitle": userTitle})

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
        if response.__contains__(False):
            return render(request, 'shell/loginError.html', {'res': response[0]})
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
        users = USER.objects.all()
        assistants = []
        for user in users:
            if user.permission.__contains__('4'):
                assistants.append([user.id, user.username])

        labQuery = LAB_SECTION.objects.all()
        labs = []
        for lab in labQuery:
            labs.append([lab.id, lab.name, lab.courseID, lab.labNumber, lab.time,
                         lab.location])

        query = A_LIST.objects.all()
        associations = []
        for entry in query:
            associations.append([entry.assistantID, entry.labID])

        return render(request, 'shell/assignAssistantToLab.html', {"assistants": assistants, "labs": labs,
                                                                   "associations": associations})

    def post(self, request):
        terminalInstance = Terminal()
        user = USER.objects.get(id=request.session['userid'])
        terminalInstance.login(user.username, user.password)

        labid = request.POST['LabId']
        assistantid = request.POST['AssistantId']
        ret, success = terminalInstance.assignAssistantToLab(int(labid), int(assistantid))

        if success is False:
            return render(request, 'shell/error.html', {"message": ret})

        return redirect('/commands/')


class assignAssistantToCourse(View):
    def get(self, request):
        users = USER.objects.all()
        assistants = []
        for user in users:
            if user.permission.__contains__('4'):
                assistants.append([user.id, user.username])

        courseQuery = COURSE.objects.all()
        courses = []
        for course in courseQuery:
            courses.append([course.id, course.name, course.courseNumber, course.classNumber, course.time,
                           course.location])

        query = I_LIST.objects.all()
        associations = []
        for entry in query:
            associations.append([entry.instructorID, entry.courseID])

        return render(request, 'shell/assignAssistantToCourse.html', {"assistants": assistants, "courses": courses,
                                                                      "associations": associations})

    def post(self, request):
        terminalInstance = Terminal()
        user = USER.objects.get(id=request.session['userid'])
        terminalInstance.login(user.username, user.password)

        Courseid = request.POST['CourseId']
        assistantid = request.POST['AssistantId']
        ret, success = terminalInstance.assignAssistantToCourse(int(Courseid), int(assistantid))

        if success is False:
            return render(request, 'shell/error.html', {"message": ret})

        return redirect('/commands/')

class assignInstructorToCourse(View):
    def get(self, request):
        terminalInstance = Terminal()
        id = request.session['userid']
        user = USER.objects.get(id=id)
        terminalInstance.login(user.username, user.password)
        ret, success = terminalInstance.accessData()
        if (success == False):
            render(request, 'shell/error.html')

        #allUsers=[]

        #for i in ret[0]:
        #    if i.permission.__contains__('3'):
        #        allUsers = allUsers + i

        allUsers = USER.objects.filter(permission='3')
        allCourses = ret[1]
        instructorAssignments = ret[4]
        return render(request, 'shell/assignInstructorToCourse.html', {'allUsers': allUsers, 'allCourses': allCourses,
                                                                       'instructorAssignments': instructorAssignments})
    def post(self, request):
        terminalInstance = Terminal()
        user = USER.objects.get(id=int(request.session['userid']))
        terminalInstance.login(user.username, user.password)
        ret, success = terminalInstance.assignInstructorToCourse(int(request.POST['courseID']), int(request.POST['instructorID']))
        if success == True:
            return redirect('/commands/')
        if success == False:
            return render(request, 'shell/error.html/', {"message": ret})

class editContactInfo(View):

  def get(self, request):
      terminalInstance = Terminal()
      id = request.session['userid']
      user = USER.objects.get(id=id)
      terminalInstance.login(user.username, user.password)
      ret, bool = terminalInstance.accessData()
      if (bool == False):
          render(request, 'shell/error.html')

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
        response, boole = terminalInstance.editContactInfo(email, contactPhone, officePhone, extension)
        if boole:
            request.method = 'get'
            return redirect('/commands/')
        else:
            return redirect('shell/createAccountError.html')

class EditCourse(View):
    def get(self, request):
        terminalInstance = Terminal()
        id = request.session['userid']
        user = USER.objects.get(id=id)
        terminalInstance.login(user.username, user.password)
        ret, bool = terminalInstance.accessData()
        if(bool == True):
            allCourses = ret[1]
            return render(request, 'shell/editCourse.html', {"allCourses": allCourses})
        return render(request, 'shell/editCourse.html')
    def post(self, request):
        terminalInstance = Terminal()
        user = USER.objects.get(id=request.session['userid'])
        terminalInstance.login(user.username, user.password)
        id = request.POST['courseid']
        name = request.POST['coursename']
        coursenumber = request.POST['coursenumber']
        classnumber = request.POST['classnumber']
        classtime = request.POST['time']
        location = request.POST['location']
        terminalInstance.editCourse(id, name, coursenumber, classnumber, classtime, location)
        return redirect('/commands/')

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

        ret, success = terminalInstance.createCourse(request.POST['name'], request.POST['courseNumber'],
                                                     request.POST['classNumber'], request.POST['time'],
                                                     request.POST['location'])

        if success is False:
            return render(request, 'shell/error.html', {"message": ret})

        return redirect('/commands/')


class createLab(View):
    def get(self, request):
        terminalInstance = Terminal()
        id = request.session['userid']
        user = USER.objects.get(id=id)
        terminalInstance.login(user.username, user.password)
        ret, bool = terminalInstance.accessData()
        if (bool == False):
            render(request, 'shell/error.html')

        allCourses = ret[1]
        return render(request, 'shell/createLab.html', {'allCourses': allCourses})

    def post(self, request):
        terminalInstance = Terminal()
        user = USER.objects.get(id=request.session['userid'])
        terminalInstance.login(user.username, user.password)

        ret, success = terminalInstance.createLab(request.POST['name'], int(request.POST['courseID']),
                                                  request.POST['labNumber'], request.POST['time'],
                                                  request.POST['location'])

        if success is False:
            return render(request, 'shell/error.html', {"message": ret})

        return redirect('/commands/')


class editLab(View):
    def get(self, request):
        labs = LAB_SECTION.objects.all()
        labList = []

        for lab in labs:
            labList.append([lab.id, lab.name, lab.courseID, lab.labNumber, lab.time, lab.location])

        return render(request, 'shell/editLab.html', {"labs": labList})

    def post(self, request):
        terminalInstance = Terminal()
        user = USER.objects.get(id=request.session['userid'])
        terminalInstance.login(user.username, user.password)

        ret, success = terminalInstance.editLab(int(request.POST['labID']), request.POST['name'], "",
                                                request.POST['labNumber'], request.POST['time'],
                                                request.POST['location'])

        if success is False:
            return render(request, 'shell/error.html', {"message": ret})

        return redirect('/commands/')


class deleteAccount(View):
    def get(self, request):
        users = USER.objects.all()
        accountList = []

        for user in users:
            accountList.append([user.id, user.username])

        return render(request, 'shell/deleteAccount.html', {"accountList": accountList})

    def post(self, request):
        terminalInstance = Terminal()
        user = USER.objects.get(id=request.session['userid'])
        terminalInstance.login(user.username, user.password)

        ret, success = terminalInstance.deleteAccount(request.POST['accountID'])

        if success is False:
            return render(request, 'shell/error.html', {"message": ret})

        return redirect('/commands/')


class deleteCourse(View):
    def get(self, request):
        courses = COURSE.objects.all()
        courseList = []

        for course in courses:
            courseList.append([course.id, course.name, course.courseNumber, course.classNumber, course.time,
                              course.location])

        return render(request, 'shell/deleteCourse.html', {"courseList": courseList})

    def post(self, request):
        terminalInstance = Terminal()
        user = USER.objects.get(id=request.session['userid'])
        terminalInstance.login(user.username, user.password)

        ret, success = terminalInstance.deleteCourse(request.POST['courseID'])

        if success is False:
            return render(request, 'shell/error.html', {"message": ret})

        return redirect('/commands/')

class deleteLab(View):
    def get(self, request):
        labs = LAB_SECTION.objects.all()
        labList = []

        for lab in labs:
            labList.append([lab.id, lab.name, lab.courseID, lab.labNumber, lab.time, lab.location])

        return render(request, 'shell/deleteLab.html', {"labs": labList})

    def post(self, request):
        terminalInstance = Terminal()
        user = USER.objects.get(id=request.session['userid'])
        terminalInstance.login(user.username, user.password)

        ret, success = terminalInstance.deleteLab(int(request.POST['labID']))

        if success is False:
            return render(request, 'shell/error.html', {"message": ret})

        return redirect('/commands/')


class viewCourses(View):
    def get(self, request):
        terminalInstance = Terminal()
        user = USER.objects.get(id=request.session['userid'])
        terminalInstance.login(user.username, user.password)
        courseAssociations = I_LIST.objects.filter(instructorID=user.id)
        courseList = []

        for entry in courseAssociations:
            course = COURSE.objects.get(id=entry.courseID)
            courseList.append([course.id, course.name, course.courseNumber, course.classNumber, course.time,
                               course.location])

        return render(request, 'shell/viewCourses.html', {"courseList": courseList})


class viewAssistants(View):
    def get(self, request):
        terminalInstance = Terminal()
        user = USER.objects.get(id=request.session['userid'])
        terminalInstance.login(user.username, user.password)

        courseAssociations = I_LIST.objects.all()
        labAssociations = A_LIST.objects.all()
        instructorCourses = []
        assistantAssociations = []

        for entry in courseAssociations:
            if int(entry.instructorID) is user.id:
                instructorCourses.append(int(entry.courseID))

        for entry in courseAssociations:
            if instructorCourses.__contains__(entry.courseID):
                assistantAssociations.append(int(entry.instructorID))

        assistants = []
        assignments = []
        allUsers = USER.objects.all()
        for user in allUsers:
            if assistantAssociations.__contains__(user.id):
                assistants.append([user.id, user.username])
                for entry in labAssociations:
                    if entry.assistantID is user.id:
                        assignments.append([user.id, user.username, entry.labID])

        courses = []
        labs = []
        for courseID in instructorCourses:
            course = COURSE.objects.get(id=courseID)
            courses.append([course.id, course.name, course.courseNumber, course.classNumber, course.time,
                           course.location])

            try:
                labQuery = LAB_SECTION.objects.filter(courseID=courseID)
                for lab in labQuery:
                    labs.append([lab.id, lab.name, lab.courseID, lab.labNumber, lab.time, lab.location])
            except LAB_SECTION.DoesNotExist:
                pass

        return render(request, 'shell/viewAssistants.html', {"assistants": assistants, "assignments": assignments, "courses": courses, "labs": labs})

class instructorAssignAssistant(View):
    def get(self, request):
        terminalInstance = Terminal()
        user = USER.objects.get(id=request.session['userid'])
        terminalInstance.login(user.username, user.password)

        aList = A_LIST.objects.all()
        iList = I_LIST.objects.all()

        instructorCourses = []
        for entry in iList:
            if entry.instructorID is user.id:
                instructorCourses.append(entry.courseID)

        instructorAssistants = []
        for entry in iList:
            if instructorCourses.__contains__(entry.instructorID) and entry.instructorID != user.id:
                instructorAssistants.append(entry.instructorID)

        assistantAssignments = []
        for entry in aList:
            if instructorAssistants.__contains__(entry.assistantID):
                assistantAssignments.append([entry.assistantID, entry.labID])

        allCourses = COURSE.objects.all()
        courseList = []
        for course in allCourses:
            if instructorCourses.__contains__(course.id):
                courseList.append([course.id, course.name, course.courseNumber, course.classNumber, course.time,
                                  course.location])

        allLabs = LAB_SECTION.objects.all()
        labList = []
        for lab in allLabs:
            if instructorCourses.__contains__(int(lab.courseID)):
                labList.append([lab.id, lab.name, lab.courseID, lab.labNumber, lab.time, lab.location])

        allUsers = USER.objects.all()
        assistantList = []
        for entry in allUsers:
            if instructorAssistants.__contains__(entry.id):
                assistantList.append([entry.id, entry.firstName, entry.lastName])

        return render(request, 'shell/instructorAssignAssistantToLab.html/', {"courseList": courseList,
                                                                              "labList": labList,
                                                                              "assistants": assistantList,
                                                                              "assistantAssignments": assistantAssignments})

    def post(self, request):
        terminalInstance = Terminal()
        user = USER.objects.get(id=request.session['userid'])
        terminalInstance.login(user.username, user.password)

        ret, success = terminalInstance.assignAssistantToLab(request.POST['labID'], request.POST['assistantID'])

        if success is False:
            return render(request, 'shell/error.html', {"message": ret})

        return redirect('/commands/')


class viewContactInfo(View):
    def get(self, request):
        terminalInstance = Terminal()
        id = request.session['userid']
        user = USER.objects.get(id=id)
        terminalInstance.login(user.username, user.password)
        allUsers, bool = terminalInstance.viewContactInfo()
        if (bool == False):
            render(request, 'shell/error.html')

        return render(request, 'shell/viewContactInfo.html', {"allUsers": allUsers})
