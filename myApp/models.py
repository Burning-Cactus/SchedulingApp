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
                               "viewContactInfo" : [12, 0],
                               "help": [13, 0],
                               "editCourse": [14, 6],
                               "deleteCourse": [15, 1],
                               "editContactInfo": [16, 4],
                               "createLab" : [17,5],
                               "assignAssistantToCourse": [18, 2],
                               "me": [19, 0],
                               "editLab": [20, 6]}

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

    def createLab(self, name, courseid, labnr, time, location):
        if self.user is None:
            return "You are not logged in"

        if self.user.permission.__contains__('1') is False and self.user.permission.__contains__('2') is False:
            return "User: " + self.username + ", does not have permission to preform this action"
        newLab=LAB_SECTION()
        newLab.name = name
        newLab.courseID=courseid
        newLab.time=time
        newLab.location=location
        newLab.labNumber=labnr
        newLab.save()
        return "new Lab Created"

    def editLab(self, labid, name, courseid, labnr, time, location):
        if self.user is None:
            return "You are not logged in"

        if self.user.permission.__contains__('1') is False and self.user.permission.__contains__('2') is False:
            return "User: " + self.username + ", does not have permission to preform this action"

        try:
            lab = LAB_SECTION.objects.get(id=labid)
        except:
            return "Lab does not exist"

        if name != '~':
            lab.name = name

        if courseid != '~':
            lab.courseid = courseid

        if labnr != '~':
            lab.labnr = labnr

        if time != '~':
            lab.time = time

        if location != '~':
            lab.location = location

        lab.save()
        return "new Lab Created"

    def deleteLab(self, labID):
        pass


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

        if permission != '':
            userEntry.permission = permission

        if username != '':
            userEntry.username = username

        if password != '':
            userEntry.password = password

        if email != '':
            userEntry.email = email

        if firstName != '':
            userEntry.firstName = firstName

        if lastName != '':
            userEntry.lastName = lastName

        if contactPhone != '':
            userEntry.contactPhone = contactPhone

        if officePhone != '':
            userEntry.officePhone = officePhone

        if extension != '':
            userEntry.extension = extension

        userEntry.save()

        return "User account updated"

    def deleteAccount(self, userid):
        # Delete a user model in the database.
        if self.user is None:
            return "You are not logged in."

        if self.user.permission.__contains__('1') is False and self.user.permission.__contains__('2') is False:
            return "User: " + self.username + ", does not have permission to preform this action."

        try:
            toDelete = USER.objects.get(id=userid)
        except USER.DoesNotExist:
            return "User does not exist"

        if toDelete.id == self.user.databaseID:
            return "You cannot delete your own account"

        try:
            A_LIST.objects.filter(assistantID=userid).delete()
        except A_LIST.DoesNotExist:
            pass

        try:
            I_LIST.objects.filter(instructorID=userid).delete()
        except I_LIST.DoesNotExist:
            pass

        toDelete.delete()

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

    def editCourse(self, courseid, name, coursenumber, classnumber, time, location):

        if self.user is None:
            return "You must be logged in."
        if self.user.permission.__contains__('1')is False and self.user.permission.__contains__('2') is False:
            return "You do not have the permission to preform this action"
        try:
            current = COURSE.objects.filter(courseid=courseid)
        except COURSE.DoesNotExist:
            return "Course Not Found"

        if name != '~':
            current.name = name
        if coursenumber != '~':
            current.courseNumber = coursenumber
        if classnumber != '~':
            current.time = time
        if location != '~':
            location.location = location

        return "Course successfully edited."

    def deleteCourse(self, courseid):
        # Delete a course from the database
        if self.user is None:
            return "You must be logged in."
        if self.user.permission.__contains__('1') is False and self.user.permission.__contains__('2') is False:
            return "You do not have permissions to use this function."
        try:
            A_LIST.objects.get(labID=LAB_SECTION.objects.get(courseID=courseid))
        except A_LIST.DoesNotExist:
            pass
        except LAB_SECTION.DoesNotExist:
            pass
        try:
            I_LIST.objects.get(courseID=courseid).delete()
            COURSE.objects.get(id=courseid).delete()
            LAB_SECTION.objects.get(courseID=courseid).delete()
        except COURSE.DoesNotExist:
            return "Course Not Found"
        except I_LIST.DoesNotExist:
            pass
        except LAB_SECTION.DoesNotExist:
            pass
        return "Course successfully deleted"


    def email(self, subject, message):
        # Send out an email to notify all recipients.
        if self.user is None:
            return "You must be logged in"
        if self.user.permission.__contains__('2') or self.user.permission.__contains__('1'):
            emails = USER.objects.all().values_list('email')
        elif self.user.permission.__contains__('3'):
            emails = USER.objects.all().filter(User.User.permission.__contains__('4')).values_list('email')
        else:
            return 'You do not have the permissions for this command'
        return list(emails)

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
        allData.extend(["I_LIST", "", "user ID  |  course ID"])
        allData.append("")

        for entry in instructorAssignments:
            line = str(entry.instructorID) + "  |  " + str(entry.courseID)

            allData.append(line)
            allData.append("")

        allData.append("")

        trueAllData = [allUsers, allCourses, allLabs, assistantAssignments, instructorAssignments]

        return trueAllData

    def assignInstructorToCourse(self, courseid, instructorid):
        # Assign an instructor to a course in the database
        if self.user is None:
            return "You must be logged in."
        if self.user.permission.__contains__('1') is False:
            return "You do not have permissions to use this function."

        try:
            COURSE.objects.get(id=courseid)
        except:
            return "Course does not exist"

        try:
            instructor = USER.objects.get(id=instructorid)
        except:
            return "User does not exist"

        if instructor.permission.__contains__('3') != True:
            return "This user is not an instructor"

        joiner = I_LIST()
        joiner.courseID = courseid
        joiner.instructorID = instructorid
        joiner.save()
        return "Instructor added to Course"

    def assignAssistantToCourse(self, courseid, assistantid):
        # Assign an instructor to a course in the database
        if self.user is None:
            return "You must be logged in."
        if self.user.permission.__contains__('1') is False:
            return "You do not have permissions to use this function."

        try:
            COURSE.objects.get(id=int(courseid))
        except:
            return "Course does not exist"

        try:
            assistant = USER.objects.get(id=int(assistantid))
        except:
            return "User does not exist"

        if assistant.permission.__contains__('4') != True:
            return "This user is not an assistant"

        try:
            if I_LIST.objects.get(courseID=int(courseid), instructorID=int(assistantid)):
                return "Asssistant is already assigned to this course"
        except I_LIST.DoesNotExist:
            pass

        I_LIST.objects.create(courseID=int(courseid), instructorID=int(assistantid)).save()
        return "Assistant added to Course"


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

        if assistant.permission.__contains__('4') != True:
            return "This user is not an assistant"

        entry = A_LIST()
        entry.labID = lab.id
        entry.assistantID = assistant.id
        entry.save()

        return "Assistant assigned to lab"

    def viewCourseAssignments(self):

        if self.user is None:
            return "You must be logged in"

        if self.user.permission.__contains__('3') is False:
            return "You don't have permission for this command."

        output = []

        # try:
        #    I_LIST.objects.exists(instructorID=self.user.databaseID)
        # except I_LIST.DoesNotExist:
        #    return "No courses assigned yet."

        if I_LIST.objects.filter(instructorID=self.user.databaseID).exists() is False:
            return "No courses assigned yet."

        instructorAssignments = I_LIST.objects.filter(instructorID=self.user.databaseID)

        for temp in instructorAssignments:
            course = COURSE.objects.get(id=temp.courseID)
            output.append(str(course.id) + "-" + course.name)

        return output


    def viewAssistantAssignments(self):

        if self.user is None:
            return "You must be logged in"

        if self.user.permission.__contains__('4'):
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

        if self.user.permission.__contains__('3'):
            assistantAssignments = []

            try:
                instructorCourses = I_LIST.objects.filter(id=self.user.databaseID)
            except:
                return "You are not assigned to any courses"

            courses = []
            for entry in instructorCourses:
                courses.append(entry.courseID)

            for element in courses:
                try:
                    assistant = I_LIST.objects.filter(courseID=element)
                    if assistant:
                        assistantAssignments.append(assistant.instructorID + ": " + USER.objects.get(id=assistant.instructorID).lastName)
                except:
                    pass

            if len(assistantAssignments) == 0:
                return "You do not have any Assistants"

            return assistantAssignments



    def viewContactInfo(self):
        # Return the contact info of the user.
        # Return the contact info of the user.
        # pull the user data from table by the id
        if self.user is None:
            return "You must be logged in"

        try:
            user = USER.objects.all()
        except user.DoesNotExist:
            return "User does not exist"
        # Assign the data to local variables
        publicInfo = []
        for entry in user:
            fname = entry.firstName
            lname = entry.lastName
            email = entry.email
            phone = entry.contactPhone
            ext = entry.extension
            publicInfo.append(fname + " " + " " + lname + " " + email + " " + phone + " " + ext)
            publicInfo.append("")



        return publicInfo

    def help(self):
        helpManual = ["","Possible Commands:", "", "",
                      "login(username, password)", "",
                      "logout()", "",
                      "me", "",
                      "createAccount([[permission]], username, password, email, firstName, lastName, contactPhone, officePhone, extension)", "",
                      "editAccount( userID, [[permission]], username, password, email, firstName, lastName, contactPhone, officePhone, extension)", "",
                      "deleteAccount(userID)", "",
                      "createCourse(name, course number, class number, time, location)", "",
                      "editCourse(course id, name, course number, class number, time, location)", "",
                      "createLab(name, course, lab number, time, location)", "",
                      "deleteCourse(course id)", "",
                      "email(subject, [message])", "",
                      "accessData()", "",
                      "assignInstructorToCourse(courseID, instructorID)", "",
                      "assignAssistantToCourse(courseID, assistantID)", "",
                      "assignAssistantToLab(assistantID, labID)", "",
                      "viewCourseAssignments()", "",
                      "viewAssistantAssignments()", "",
                      "viewContactInfo(userID)"  "",  "",
                      "editContactInfo(email, contactPhone, officePhone, extension)",""]

        return helpManual

    def editContactInfo(self, email, contactPhone, officePhone, extension):

        if self.user is None:
            "You must be logged in"

        if email != '~':
            self.user.email = email

        if contactPhone != '~':
            self.user.contactPhone = contactPhone

        if officePhone != '~':
            self.user.officePhone = officePhone

        if extension != '~':
            self.user.extenstion = extension

        userEntry = USER.objects.get(id=self.user.databaseID)

        userEntry.email = self.user.email
        userEntry.contactPhone = self.user.contactPhone
        userEntry.officePhone = self.user.officePhone
        userEntry.extension = self.user.extension
        userEntry.save()

        return "Contact information updated"

    def me(self):

        if self.user is None:
            return "You are not logged in"

        myAccount = ['',"Permission: " + self.user.permission, '', "Username: " + self.user.username, '', "Password: " + self.user.password, '',
                     "email: " + self.user.email, '', "First Name: " + self.user.firstName, '', "Last Name: " + self.user.lastName, '',
                     "Contact Phone: " + self.user.contactPhone, '', "Office Phone: " + self.user.officePhone, '',
                     "Extension: " + self.user.extension,'']

        return myAccount

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
            return self.viewContactInfo()

        if commandIntegerCode == 13:
            return self.help()

        if commandIntegerCode == 14:
            return self.editCourse(argumentList[0], argumentList[1], argumentList[2], argumentList[3], argumentList[4],
                                   argumentList[5])

        if commandIntegerCode == 15:
            return self.deleteCourse(argumentList[0])

        if commandIntegerCode == 16:
            return self.editContactInfo(argumentList[0], argumentList[1], argumentList[2], argumentList[3])

        if commandIntegerCode == 17:
            return self.createLab(argumentList[0], argumentList[1], argumentList[2],
                                  argumentList[3], argumentList[4])

        if commandIntegerCode == 18:
            return self.assignAssistantToCourse(argumentList[0], argumentList[1])

        if commandIntegerCode == 19:
            return self.me()

        if commandIntegerCode == 20:
            return self.editLab(argumentList[0], argumentList[1], argumentList[2],
                                argumentList[3], argumentList[4], argumentList[5])
