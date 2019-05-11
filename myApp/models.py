from django.db import models
from ScheduleApp import User, Course
import re
from django.core.mail import send_mail
from .Parser import *
# Create your models here.


class USER(models.Model):
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    permission = models.CharField(max_length=10)
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
            return ["Command not found: " + inStr, "Try: help"], False

        if len(argumentList) == commandLabelOptions[commandLabel][1]:
            ret, bool = self.callCommand(commandLabelOptions[commandLabel][0], argumentList)
            return ret, bool
        else:
            return ["Command argument mismatch: " + inStr, "Try: help", commandLabel, argumentList], False

    def login(self, xName, xPassword):

        try:
            userData = USER.objects.get(username=xName)
        except USER.DoesNotExist:
            return "Invalid username or password", False

        if(userData.password == xPassword):
            self.user = User.User(userData.permission, userData.username, userData.password,
                                  userData.id, userData.email, userData.firstName, userData.lastName,
                                  userData.contactPhone, userData.officePhone, userData.extension)
            self.username = self.user.username
        else:
            return "Invalid username or password", False
        return "Logged in as: " + self.username, True

    def logout(self):
        username = self.username
        self.user = None
        self.username = ""
        return username + " has been logged out", True

    def createLab(self, name, courseid, labnr, time, location):
        if self.user is None:
            return "You are not logged in", False

        if (name == "" or None) or (courseid == "" or None) or (labnr == "" or None) or (time == "" or None) or (location == "" or None):
            return "Fields Missing", False

        if self.user.permission.__contains__('1') is False and self.user.permission.__contains__('2') is False:
            return "User: " + self.username + ", does not have permission to preform this action", False

        try:
            if LAB_SECTION.objects.get(labNumber=labnr):
                return 'Lab Number Already Used', False
        except LAB_SECTION.DoesNotExist:
            pass

        try:
            COURSE.objects.get(id=courseid)
        except COURSE.DoesNotExist:
            return "Course Does not exist", False

        newLab=LAB_SECTION()
        newLab.name = name
        newLab.courseID=courseid
        newLab.time=time
        newLab.location=location
        newLab.labNumber=labnr
        newLab.save()
        return "new Lab Created", True

    def editLab(self, labid, name, courseid, labnr, time, location):
        if self.user is None:
            return "You are not logged in", False

        if self.user.permission.__contains__('1') is False and self.user.permission.__contains__('2') is False:
            return "User: " + self.username + ", does not have permission to preform this action", False

        try:
            lab = LAB_SECTION.objects.get(id=labid)
        except:
            return "Lab does not exist", False

        if name != '' or None:
            lab.name = name

        if labnr != '' or None:
            lab.labnr = labnr

        if time != '' or None:
            lab.time = time

        if location != '' or None:
            lab.location = location

        lab.save()
        return "new Lab Created", True

    def deleteLab(self, labID):

        if labID == None:
            return None, False

        if self.user.permission.__contains__("1") is False and self.user.permission.__contains__("2") is False:
            return None, False

        try:
            lab = LAB_SECTION.objects.get(id=int(labID))
        except LAB_SECTION.DoesNotExist:
            return None, False

        try:
            A_LIST.objects.filter(labID=int(labID)).delete()
        except A_LIST.DoesNotExist:
            pass

        lab.delete()

        return "Lab deleted", True


    def createAccount(self, permission, username, password, email, firstName, lastName, contactPhone, officePhone, extension):

        if self.user is None:
            return "You are not logged in", False

        if self.user.permission.__contains__('1') is False and self.user.permission.__contains__('2') is False:
            return "User: " + self.username + ", does not have permission to preform this action", False

        if (permission == "" or None) or (username == "" or None) or (password == "" or None) or (email == "" or None):
            return None, False
        if (firstName == "" or None) or (lastName == "" or None) or (contactPhone == "" or None):
            return None, False
        if (officePhone == "" or None) or (extension == "" or None):
            return None, False

        try:
            if USER.objects.get(username=username):
                return None, False
        except USER.DoesNotExist:
            pass


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
        return "New user created", True

    def editAccount(self, userid, permission, username, password, email, firstName, lastName, contactPhone, officePhone, extension):

        if self.user is None:
            return "You are not logged in", False

        if self.user.permission.__contains__('1')is False and self.user.permission.__contains__('2') is False:
            return "You do not have the permission to preform this action", False

        try:
            userEntry = USER.objects.get(id=userid)
        except:
            return "User does not exist", False

        try:
            if len(USER.objects.filter(username=username)) > 0:
                return None, False
        except USER.DoesNotExist:
            pass

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

        return "User account updated", True

    def deleteAccount(self, userid):
        # Delete a user model in the database.
        if self.user is None:
            return "You are not logged in.", False

        if self.user.permission.__contains__('1') is False and self.user.permission.__contains__('2') is False:
            return "User: " + self.username + ", does not have permission to preform this action.", False

        try:
            toDelete = USER.objects.get(id=userid)
        except USER.DoesNotExist:
            return "User does not exist", False

        if toDelete.id == self.user.databaseID:
            return "You cannot delete your own account", False

        try:
            A_LIST.objects.filter(assistantID=userid).delete()
        except A_LIST.DoesNotExist:
            pass

        try:
            I_LIST.objects.filter(instructorID=userid).delete()
        except I_LIST.DoesNotExist:
            pass
        toDelete.delete()

        return "User Deleted", True

    def createCourse(self, name, coursenumber, classnumber, time, location):
        if self.user is None:
            return "You must be logged in.", False
        if self.user.permission.__contains__('1') is False and self.user.permission.__contains__('2') is False:
            return "You do not have permissions to use this function.", False

        if (name == "" or None) or (coursenumber == "" or None) or (classnumber == "" or None) or (time == "" or None) or (location == "" or None):
            return None, False

        try:
            if COURSE.objects.get(courseNumber=coursenumber, classNumber=classnumber):
                return None, False
        except COURSE.DoesNotExist:
            pass

        COURSE.objects.create(name=name, courseNumber=coursenumber, classNumber=classnumber, time=time,
                              location=location).save()

        return "Course successfully created.", True

    def editCourse(self, courseid, name, coursenumber, classnumber, time, location):

        if self.user is None:
            return "You must be logged in.", False
        if self.user.permission.__contains__('1')is False and self.user.permission.__contains__('2') is False:
            return "You do not have the permission to preform this action", False
        try:
            current = COURSE.objects.get(id=courseid)
        except COURSE.DoesNotExist:
            return "Course Not Found", False

        if name != '' or None:
            current.name = name
        if classnumber != '' or None:
            current.classNumber = classnumber
        if time != '' or None:
            current.time = time
        if location != '' or None:
            current.location = location

        current.save()

        return "Course successfully edited.", True

    def deleteCourse(self, courseid):
        # Delete a course from the database
        if self.user is None:
            return "You must be logged in.", False
        if self.user.permission.__contains__('1') is False and self.user.permission.__contains__('2') is False:
            return "You do not have permissions to use this function.", False
        try:
            labs = LAB_SECTION.objects.filter(courseID=courseid)
            for lab in labs:
                A_LIST.objects.get(labID=lab.id).delete()
        except A_LIST.DoesNotExist:
            pass
        except LAB_SECTION.DoesNotExist:
            pass
        try:
            I_LIST.objects.filter(courseID=courseid).delete()
            LAB_SECTION.objects.filter(courseID=courseid).delete()
            COURSE.objects.get(id=courseid).delete()
        except COURSE.DoesNotExist:
            return "Course Not Found", False
        except I_LIST.DoesNotExist:
            pass
        except LAB_SECTION.DoesNotExist:
            pass

        return "Course successfully deleted", True


    def email(self, subject, message):
        # Send out an email to notify all recipients.
        if self.user is None:
            return "You must be logged in", False
        if self.user.permission.__contains__('2') or self.user.permission.__contains__('1'):
            try:
                emails = USER.objects.all().values_list('email')
            except USER.DoesNotExistL:
                pass
        elif self.user.permission.__contains__('3'):
            try:
                emails = USER.objects.all().filter(USER.permission.__contains__('4')).values_list('email')
            except USER.DoesNotExist:
                pass
        else:
            return 'You do not have the permissions for this command'
        return list(emails), True

    def accessData(self):

        if self.user is None:
            return "You must be logged in", False

        if self.user.permission.__contains__('1') is False and self.user.permission.__contains__('2') is False:
            return "User: " + self.username + ", does not have permission to preform this action", False

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

        return [allUsers, allCourses, allLabs, assistantAssignments, instructorAssignments], True

    def assignInstructorToCourse(self, courseid, instructorid):
        # Assign an instructor to a course in the database
        if self.user is None:
            return "You must be logged in.", False
        if self.user.permission.__contains__('1') is False:
            return "You do not have permissions to use this function.", False

        try:
            COURSE.objects.get(id=int(courseid))
        except:
            return "Course does not exist", False

        try:
            instructor = USER.objects.get(id=int(instructorid))
        except:
            return "User does not exist", False

        try:
            if I_LIST.objects.get(courseID=int(courseid), instructorID=int(instructorid)):
                return None, False
        except I_LIST.DoesNotExist:
            pass

        if instructor.permission.__contains__('3') != True:
            return "This user is not an instructor", False

        I_LIST.objects.create(courseID=courseid, instructorID=instructorid).save()

        return "Instructor added to Course", True

    def assignAssistantToCourse(self, courseid, assistantid):

        if self.user is None:
            return "You must be logged in.", False
        if self.user.permission.__contains__('1') is False:
            return "You do not have permissions to use this function.", False

        try:
            COURSE.objects.get(id=int(courseid))
        except:
            return "Course does not exist", False

        try:
            assistant = USER.objects.get(id=int(assistantid))
        except:
            return "User does not exist", False

        if assistant.permission.__contains__('4') != True:
            return "This user is not an assistant", False

        try:
            if I_LIST.objects.get(courseID=int(courseid), instructorID=int(assistantid)):
                return "Asssistant is already assigned to this course", False
        except I_LIST.DoesNotExist:
            pass

        I_LIST.objects.create(courseID=int(courseid), instructorID=int(assistantid)).save()
        return "Assistant added to Course", True


    def assignAssistantToLab(self, labid, assistantid):

        if self.user is None:
            return "You must be logged in", False

        if self.user.permission.__contains__("1") is False and self.user.permission.__contains__("3") is False:
            return "You do not have the permissions to preform this action", False

        try:
            lab = LAB_SECTION.objects.get(id=int(labid))
        except:
            return "Lab does not exist", False

        try:
            assistant = USER.objects.get(id=int(assistantid))
        except:
            return "User does not exist", False

        if assistant.permission.__contains__('4') != True:
            return "This user is not an assistant", False

        try:
            if A_LIST.objects.get(labID=int(labid), assistantID=int(assistantid)):
                return "Assistant already assigned to lab", False
        except A_LIST.DoesNotExist:
            pass

        A_LIST.objects.create(labID=int(labid), assistantID=int(assistantid)).save()

        return "Assistant assigned to lab", True

    def viewCourseAssignments(self):

        if self.user is None:
            return "You must be logged in", False

        if self.user.permission.__contains__('3') is False:
            return "You don't have permission for this command.", False

        output = []

        # try:
        #    I_LIST.objects.exists(instructorID=self.user.databaseID)
        # except I_LIST.DoesNotExist:
        #    return "No courses assigned yet."

        if I_LIST.objects.filter(instructorID=self.user.databaseID).exists() is False:
            return "No courses assigned yet.", False

        instructorAssignments = I_LIST.objects.filter(instructorID=self.user.databaseID)

        for temp in instructorAssignments:
            course = COURSE.objects.get(id=temp.courseID)
            output.append(str(course.id) + "-" + course.name)

        return output, True


    def viewAssistantAssignments(self):

        if self.user is None:
            return "You must be logged in", False

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

            return assistantAssignments, True

        if self.user.permission.__contains__('3'):
            assistantAssignments = []

            try:
                instructorCourses = I_LIST.objects.filter(id=self.user.databaseID)
            except:
                return "You are not assigned to any courses", False

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
                return "You do not have any Assistants", False

            return assistantAssignments, True



    def viewContactInfo(self):
        # Return the contact info of the user.
        # Return the contact info of the user.
        # pull the user data from table by the id
        if self.user is None:
            return "You must be logged in", False

        try:
            user = USER.objects.all()
        except user.DoesNotExist:
            return "User does not exist", False
        # Assign the data to local variables
        allUsers = USER.objects.all()

        return allUsers, True

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
            "You must be logged in", False

        if email != '~':
            self.user.email = email

        if contactPhone != '~':
            self.user.contactPhone = contactPhone

        if officePhone != '~':
            self.user.officePhone = officePhone

        if extension != '~':
            self.user.extension = extension

        userEntry = USER.objects.get(id=self.user.databaseID)

        userEntry.email = self.user.email
        userEntry.contactPhone = self.user.contactPhone
        userEntry.officePhone = self.user.officePhone
        userEntry.extension = self.user.extension
        userEntry.save()

        return "Contact information updated", True

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
