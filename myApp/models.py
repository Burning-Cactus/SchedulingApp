from django.db import models
from ScheduleApp import User, Course
import re
from django.core.mail import send_mail
from .Parser import *
# Create your models here.


class USER(models.Model):
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    permission = models.CharField(max_length=5)
    email = models.CharField(max_length=60)
    firstName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    contactPhone = models.CharField(max_length=12)
    officePhone = models.CharField(max_length=12)
    extension = models.CharField(max_length=5)


class LAB_SECTION(models.Model):
    name = models.CharField(max_length=60)
    labNumber = models.CharField(max_length=60)
    courseID = models.CharField(max_length=60)
    time = models.CharField(max_length=60)
    location = models.CharField(max_length=60)


class A_LIST(models.Model):
    assistantID = models.IntegerField()
    labID = models.IntegerField()


class COURSE(models.Model):
    name = models.CharField(max_length=60)
    courseNumber = models.CharField(max_length=60)
    classNumber = models.CharField(max_length=60)
    time = models.CharField(max_length=60)
    location = models.CharField(max_length=60)


class I_LIST(models.Model):
    instructorID = models.IntegerField()
    courseID = models.IntegerField()


class Terminal(object):
    # This class will be used to execute commands with the database.
    user = None

    # to avoid null pointer when rendering self.user.username
    username = ""
    def command(self, inStr):

        # each key has a list, each list has a commandIntegerCode at [0]
        # and the amount of arguments that the command takes at [1]
        commandLabelOptions = {"login" : [0, 2],
                               "logout" : [1, 0],
                               "createAccount" : [2, 9],
                               "editAccount" : [3, 10],
                               "deleteAccount" : [4, 1],
                               "createCourse" : [5, 5],
                               "email" : [6, 2],
                               "accessData" : [7, 0],
                               "assignInstructorToCourse" : [8, 2],
                               "assignAssistantToLab" : [9, 2],
                               "viewCourseAssignments" : [10, 0],
                               "viewAssistantAssignments" : [11, 0],
                               "viewContactInfo" : [12, 1],
                               "help": [13, 0],
                               "editCourse": [14, 0],
                               "deleteCourse": [15, 0],
                               "editContactInfo": [16, 4]}

        parser = Parser()
        parser.parseCommand(inStr)

        commandLabel = parser.commandLabel
        argumentList = parser.argumentList

        if commandLabelOptions.__contains__(commandLabel) is False:
            return ["Command not found: " + inStr, "Try: help"]

        if len(argumentList) == commandLabelOptions[commandLabel][1]:
            return self.callCommand(commandLabelOptions[commandLabel][0], argumentList)
        else:
            return ["Command argument mismatch: " + inStr, "Try: help", commandLabel, argumentList]

    def login(self, xName, xPassword):

        try:
            userData = USER.objects.get(username=xName)
        except USER.DoesNotExist:
            return "Invalid username or password"

        if(userData.password == xPassword):
            self.user = User.User(userData.permission, userData.username, userData.password,
                                  userData.id, userData.email, userData.firstName, userData.lastName,
                                  userData.contactPhone, userData.officePhone, userData.extension)
            self.username = self.user.username
        else:
            return "Invalid username or password"
        return "Logged in as: " + self.username

    def logout(self):
        username = self.username
        self.user = None
        self.username = ""
        return username + " has been logged out"

    def createAccount(self, permission, username, password, email, firstName, lastName, contactPhone, officePhone, extension):

        if self.user is None:
            return "You are not logged in"

        if self.user.permission.__contains__('1') is False and self.user.permission.__contains__('2') is False:
            return "User: " + self.username + ", does not have permission to preform this action"

        newUser = USER()
        newUser.permission = permission
        newUser.username = username
        newUser.password = password
        newUser.email = email
        newUser.firstName = firstName
        newUser.lastName = lastName
        newUser.contactPhone = contactPhone
        newUser.officePhone = officePhone
        newUser.extension = extension
        newUser.save()
        return "New user created"

    def editAccount(self, userid, permission, username, password, email, firstName, lastName, contactPhone, officePhone, extension):

        if self.user is None:
            return "You are not logged in"

        if self.user.permission.__contains__('1')is False and self.user.permission.__contains__('2') is False:
            return "You do not have the permission to preform this action"

        try:
            userEntry = USER.objects.get(id=userid)
        except:
            return "User does not exist"

        if permission != '~':
            userEntry.permission = permission

        if username != '~':
            userEntry.username = username

        if password != '~':
            userEntry.password = password

        if email != '~':
            userEntry.email = email

        if firstName != '~':
            userEntry.firstName = firstName

        if lastName != '~':
            userEntry.lastName = lastName

        if contactPhone != '~':
            userEntry.contactPhone = contactPhone

        if officePhone != '~':
            userEntry.officePhone = officePhone

        if extension != '~':
            userEntry.extension = extension

        userEntry.save()

        return "User account updated"

    def deleteAccount(self, userid):
        # Delete a user model in the database.
        if self.user is None:
            return "You are not logged in."

        if self.user.permission.__contains__('1') is False and self.user.permission.__contains__('2') is False:
            return "User: " + self.username + ", does not have permission to preform this action."

        # Whiteout what is already there
        self.user.permission = None

        # i_list and a_list references deleted too
        try:
            A_LIST.objects.filter(assistantID=userid).delete()
        except A_LIST.DoesNotExist:
            return "Assistant Not in A_LIST"
        try:
            I_LIST.objects.filter(instructorID=userid).delete()
        except I_LIST.DoesNotExist:
            return "Instructor Not in I_LIST"

        # Ladies and gentlemen, we got 'em.
        return "User Deleted"

    def createCourse(self, name, coursenumber, classnumber, time, location):
        if self.user is None:
            return "You must be logged in."
        if self.user.permission.__contains__('1') is False and self.user.permission.__contains__('2') is False:
            return "You do not have permissions to use this function."
        course = COURSE()
        course.name = name
        course.courseNumber = coursenumber
        course.classNumber = classnumber
        course.time = time
        course.location = location
        course.save()
        return "Course successfully created."

    def editCourse(self, name, coursenumber, classnumber, time, location):
        return "this isn't made yet"

    def deleteCourse(self, coursenumber, classnumber):
        # Delete a course from the database
        if self.user is None:
            return "You must be logged in."
        if self.user.permission.__contains__('1') is False and self.user.permission.__contains__('2') is False:
            return "You do not have permissions to use this function."
        try:
            COURSE.objects.filter(courseNumber=coursenumber, classNumber=classnumber).delete()
        except COURSE.DoesNotExist:
            return "Course Not Found"
        return "Course successfully deleted"

    def email(self, subject, message):
        # Send out an email to notify all recipients.
        if self.user is None:
            return "You must be logged in"
        if self.user.permission.__contains__('2'):
            emails = USER.objects.all().values_list('email')
            send_mail(
                subject,
                message,
                USER.email,
                emails)
        elif self.user.permission.__contains__('3'):
            emails = USER.objects.all().filter(User.User.permission.__contains__('4')).values_list('email')
            send_mail(
                subject,
                message,
                USER.email,
                emails)
        else:
            return 'You do not have the permissions for this command'
        return "e-mail sent"

    def accessData(self):

        if self.user is None:
            return "You must be logged in"

        if self.user.permission.__contains__('1') is False and self.user.permission.__contains__('2') is False:
            return "User: " + self.username + ", does not have permission to preform this action"

        allUsers = []
        allCourses = []
        allLabs = []
        assistantAssignments = []
        instructorAssignments = []

        if USER.objects.count() == 0:
            pass
        else:
            allUsers = USER.objects.all()

        if COURSE.objects.count() == 0:
            pass
        else:
            allCourses = COURSE.objects.all()

        if LAB_SECTION.objects.count() == 0:
            pass
        else:
            allLabs = LAB_SECTION.objects.all()

        if A_LIST.objects.count() == 0:
            pass
        else:
            assistantAssignments = A_LIST.objects.all()

        if I_LIST.objects.count() == 0:
            pass
        else:
            instructorAssignments = I_LIST.objects.all()

        allData = ["USER", "", "ID  |  permission  |  username  |  password  |  first name  |  "
                               "last name  |  email  |  contact phone  |  office phone  |  extension"]

        for entry in allUsers:
            line = str(entry.id) + "  |  " + str(entry.permission) + "  |  " + str(entry.username) + "  |  " + \
                   str(entry.password) + "  |  " + str(entry.firstName) + "  |  " + str(entry.lastName) + "  |  " + \
                   str(entry.email) + "  |  " + str(entry.contactPhone) + "  |  " + str(entry.officePhone) + "  |  " + \
                   str(entry.extension)

            allData.append(line)
            allData.append("")

        allData.append("")
        allData.extend(["COURSE", "", "ID  |  name  |  course number  |  class number  |  time  |  location"])
        allData.append("")

        for entry in allCourses:
            line = str(entry.id) + "  |  " + str(entry.name) + "  |  " + str(entry.courseNumber) + "  |  " + \
                   str(entry.classNumber) + "  |  " + str(entry.time) + "  |  " + str(entry.location)

            allData.append(line)
            allData.append("")

        allData.append("")
        allData.extend(["LAB_SECTION", "", "ID  |  name  |  lab number  |  course ID  |  time  |  location"])
        allData.append("")

        for entry in allLabs:
            line = str(entry.id) + "  |  " + str(entry.name) + "  |  " + str(entry.labNumber) + "  |  " + \
                   str(entry.courseID) + "  |  " + str(entry.time) + "  |  " + str(entry.location)

            allData.append(line)
            allData.append("")

        allData.append("")
        allData.extend(["A_LIST", "", "assistant ID  |  lab ID"])
        allData.append("")

        for entry in assistantAssignments:
            line = str(entry.assistantID) + "  |  " + str(entry.labID)

            allData.append(line)
            allData.append("")

        allData.append("")
        allData.extend(["I_LIST", "", "instructor ID  |  lab ID"])
        allData.append("")

        for entry in instructorAssignments:
            line = str(entry.instructorID) + "  |  " + str(entry.courseID)

            allData.append(line)
            allData.append("")

        allData.append("")

        return allData

    def assignInstructorToCourse(self, courseid, instructorid):
        # Assign an instructor to a course in the database
        if self.USER is None:
            return "You must be logged in."
        if self.user.permission.__contains('1') is False:
            return "You do not have permissions to use this function."
        try:
            USER.objects.get(id=instructorid).courseID = models.ForeignKey(COURSE.objects.get(id=courseid),
                                                                           on_delete=models.SET(None))
            COURSE.objects.get(id=courseid).instructorID = models.ForeignKey(USER.objects.get(id=instructorid),
                                                                             on_delete=models.SET(None))
        except USER.DoesNotExist:
            return "User does not exist"
        except COURSE.DoesNotExist:
            return "Course does ot exist"

        joiner = I_LIST()
        joiner.courseID.save()
        joiner.instructorID.save()
        return "Instructor added to Course"


    def assignAssistantToLab(self, labid, assistantid):

        if self.user is None:
            return "You must be logged in"

        if self.user.permission.__contains__("1") is False:
            return "You do not have the permissions to preform this action"

        try:
            lab = COURSE.objects.get(id=labid)
        except:
            return "Course does not exist"

        try:
            assistant = USER.objects.get(id=assistantid)
        except:
            return "User does not exist"

        entry = A_LIST()

        entry.labID = lab
        entry.assistantID = assistant

        return "Assistant assigned to lab"

    def viewCourseAssignments(self):

        if self.user is None:
            return "You must be logged in"

        instructorAssignments = []
        courses = []
        output = []

        try:
            instructorAssignments = I_LIST.objects.get(id=self.user.databaseID)
        except(I_LIST.DoesNotExist):
            return "No courses assigned yet."


        for temp in instructorAssignments:
            course = COURSE.objects.get(id=temp.courseID)
            output.append(course.id + "-" + course.name)

        return output


    def viewAssistantAssignments(self):

        if self.user is None:
            return "You must be logged in"

        assistantAssignments = []
        entry = []

        if A_LIST.objects.count() == 0:
            pass
        else:
            entry = A_LIST.objects.all()

        assistantAssignments.append("")
        assistantAssignments.extend(["A_LIST", "", "assistant ID  |  lab ID"])
        assistantAssignments.append("")

        for entry in assistantAssignments:
            line = str(entry.assistantID) + "  |  " + str(entry.labID)

            assistantAssignments.append(line)
            assistantAssignments.append("")

        return assistantAssignments

    def viewContactInfo(self, userid):
        # Return the contact info of the user.
        # Return the contact info of the user.
        # pull the user data from table by the id
        if self.user is None:
            return "You must be logged in"
        if self.user.permission.__contains__('4'):
            try:
                user = USER.objects.get(id=userid)
            except user.DoesNotExist:
                return "User does not exist"
            # Assign the data to local variables
            fname = user.firstName
            lname = user.lastName
            email = user.email
            phone = user.contactPhone
            ext = user.extension
            return fname + " " + " " + lname + " " + email + " " + phone + " " + ext
        else:
            return 'You do not have the permissions for this command'

    def help(self):
        helpManual = ["","Possible Commands:", "", "",
                      "login(username, password)", "",
                      "createAccount(permission, username, password, email, firstName, lastName, contactPhone, officePhone, extension)", "",
                      "editAccount(userID)", "",
                      "deleteAccount(userID)", "",
                      "createCourse(name, course number, class number, time, location)", "",
                      "editCourse(name, course number, class number, time, location)", "",
                      "deleteCourse(course number, class number)", "",
                      "email(message)", "",
                      "accessData()", "",
                      "assignInstructorToCourse(courseID, instructorID)", "",
                      "assignAssistantToCourse(courseID, assistantID)", "",
                      "viewCourseAssignments(userID)", "",
                      "viewAssistantAssignments(userID)", "",
                      "viewContactInfo(userID)"  "",  ""]

        return helpManual

    def editContactInfo(self, email, contactPhone, officePhone, extension):

        if self.user is None:
            "You must be logged in"

        if email != '~':
            self.user.setEmail(email)

        if contactPhone != '~':
            self.user.setContactPhone(contactPhone)

        if officePhone != '~':
            self.user.officePhone(officePhone)

        if extension != '~':
            self.user.setExtension(extension)

        userEntry = USER.objects.get(id=self.user.databaseID)

        userEntry.email = self.user.email
        userEntry.contactPhone = self.user.contactPhone
        userEntry.officePhone = self.user.officePhone
        userEntry.entension = self.user.extension
        userEntry.save()

        return "Contact information updated"

    # calls the command matching the integer code, using argumentList
    # from user input
    #
    # IMPORTANT: self contains the user variable, ie: self.user.permission
    # Therefore we do not need an argument for permission in any of the commands.
    # I will remove them now.
    def callCommand(self, commandIntegerCode, argumentList):

        if commandIntegerCode == 0:
            return self.login(argumentList[0], argumentList[1])

        if commandIntegerCode == 1:
            return self.logout()

        if commandIntegerCode == 2:
            return self.createAccount(argumentList[0], argumentList[1], argumentList[2],
                                      argumentList[3], argumentList[4], argumentList[5],
                                      argumentList[6], argumentList[7], argumentList[8])

        if commandIntegerCode == 3:
            return self.editAccount(argumentList[0], argumentList[1], argumentList[2],
                                    argumentList[3], argumentList[4], argumentList[5],
                                    argumentList[6], argumentList[7], argumentList[8],
                                    argumentList[9])

        if commandIntegerCode == 4:
            return self.deleteAccount(argumentList[0])

        if commandIntegerCode == 5:
            return self.createCourse(argumentList[0], argumentList[1], argumentList[2],
                              argumentList[3], argumentList[4])

        if commandIntegerCode == 6:
            return self.email(argumentList[0], argumentList[1])

        if commandIntegerCode == 7:
            return self.accessData()

        if commandIntegerCode == 8:
            return self.assignInstructorToCourse(argumentList[0], argumentList[1])

        if commandIntegerCode == 9:
            return self.assignAssistantToLab(argumentList[0], argumentList[1])

        if commandIntegerCode == 10:
            return self.viewCourseAssignments()

        if commandIntegerCode == 11:
            return self.viewAssistantAssignments()

        if commandIntegerCode == 12:
            return self.viewContactInfo(argumentList[0])

        if commandIntegerCode == 13:
            return self.help()

        if commandIntegerCode == 14:
            return self.editCourse(argumentList[0], argumentList[1], argumentList[2], argumentList[3], argumentList[4])

        if commandIntegerCode == 15:
            return self.deleteCourse(argumentList[0], argumentList[1])

        if commandIntegerCode == 16:
            return self.deleteCourse(argumentList[0], argumentList[1], argumentList[2], argumentList[3])
