from django.db import models
from ScheduleApp import User

# Create your models here.


class USER(models.Model):
    username = models.CharField(max_length = 60)
    password = models.CharField(max_length = 60)
    permission = models.CharField(max_length = 5)
    email = models.CharField(max_length = 60)
    firstName = models.CharField(max_length = 60)
    lastName = models.CharField(max_length = 60)
    contactPhone = models.CharField(max_length = 12)
    officePhone = models.CharField(max_length= 12)
    extension = models.CharField(max_length = 5)


class LAB_SECTION(models.Model):
    pass


class A_LIST(models.Model):
    pass


class COURSE(models.Model):
    pass


class I_LIST(models.Model):
    pass


class Terminal:
    # This class will be used to execute commands with the database.
    user = None
    def command(self, inStr):

        # this will get everything before the first '('
        commandLabel = inStr.split('(')[0]

        commandLabelOptions = {"login" : 0,
                               "logout" : 1,
                               "createAccount" : 2,
                               "editAccount" : 3,
                               "deleteAccount" : 4,
                               "createCourse" : 5,
                               "email" : 6,
                               "accessData" : 7,
                               "assignInstructorToCourse" : 8,
                               "assignAssistantToCourse" : 9,
                               "viewCourseAssignments" : 10,
                               "viewAssistantAssignments" : 11,
                               "viewContactInfo" : 12}

        # get the corresponding command
        commandIntegerCode = None

        if commandLabelOptions.__contains__(commandLabel):
            commandIntegerCode = commandLabelOptions.get(commandLabel)

        else:
            return "Error: Command not found"

        # parse out the command arguments
        afterCommandLabel = inStr.split('(')[1]
        betweenParenthesis = afterCommandLabel[0:len(afterCommandLabel)-1]
        argumentList = betweenParenthesis.split(',')

        # function at end of this file
        # self contains the user variable
        return self.callCommand(argumentList, commandIntegerCode)



    def login(self, xName, xPassword):

        try:
            userData = USER.objects.get(username=xName)
        except USER.DoesNotExist:
            return "Invalid username or password"

        if(userData.password == xPassword):
            self.user = User.User(userData.permission, userData.username, userData.password,
                                  userData.id, userData.email, userData.firstName, userData.lastName,
                                  userData.contactPhone, userData.officePhone, userData.extension)
        else:
            return "Invalid username or password"
        return "Logged in as: " + self.user.username

    def logout(self, xUser):
        self.user = None
        return "" + xUser + " has been logged out"

    def createAccount(self, first, last, username, password, email):
        # Create a new user in the database with all of the parameters provided and a generated ID.
        #person = User()
        #person.toString()

        # return value for testing, will change when function is implemented
        return '2'

    def editAccount(self, userid):
        # Change the values of a user in the database.

        # return value for testing, will change when function is implemented
        return '3'

    def deleteAccount(self, userid):
        # Delete a user model in the database.

        # return value for testing, will change when function is implemented
        return '4'

    def createCourse(self, name, coursenumber, classnumber, time, location):
        # Create a course in the database with a generated ID.

        # return value for testing, will change when function is implemented
        return '5'

    def email(self, message):
        # Send out an email to notify all recipients.

        # return value for testing, will change when function is implemented
        return '6'

    def accessData(self):
        # Access all data in the system and print it in tables

        # return value for testing, will change when function is implemented
        return '7'

    def assignInstructorToCourse(self, courseid, instructorid):
        # Assign an instructor to a course in the database

        # return value for testing, will change when function is implemented
        return '8'


    def assignAssistantToCourse(self, courseid, instructorid):
        # Assign a TA to a course in the database

        # return value for testing, will change when function is implemented
        return '9'

    def viewCourseAssignments(self, userid):
        # Return data on instructor assignments in the database.

        # return value for testing, will change when function is implemented
        return '10'

    def viewAssistantAssignments(self, userid):
        # Return data on TA assignments in the database

        # return value for testing, will change when function is implemented
        return '11'

    def viewContactInfo(self, userid):
        # Return the contact info of the user.

        # return value for testing, will change when function is implemented
        return '12'

    # calls the command matching the integer code, using argumentList
    # from user input
    #
    # IMPORTANT: self contains the user variable, ie: self.user.permission
    # Therefore we do not need an argument for permission in any of the commands.
    # I will remove them now.
    def callCommand(self, argumentList, commandIntegerCode):

        if commandIntegerCode == 0:
            return self.login(argumentList[0], argumentList[1])

        if commandIntegerCode == 1:
            return self.logout(argumentList[0])

        if commandIntegerCode == 2:
            return self.createAccount(argumentList[0], argumentList[1], argumentList[2],
                               argumentList[3], argumentList[4])

        if commandIntegerCode == 3:
            return self.editAccount(argumentList[0])

        if commandIntegerCode == 4:
            return self.deleteAccount(argumentList[0])

        if commandIntegerCode == 5:
            return self.createCourse(argumentList[0], argumentList[1], argumentList[2],
                              argumentList[3], argumentList[4])

        if commandIntegerCode == 6:
            return self.email(argumentList[0])

        if commandIntegerCode == 7:
            return self.accessData()

        if commandIntegerCode == 8:
            return self.assignInstructorToCourse(argumentList[0], argumentList[1])

        if commandIntegerCode == 9:
            return self.assignAssistantToCourse(argumentList[0], argumentList[1])

        if commandIntegerCode == 10:
            return self.viewCourseAssignments(argumentList[0])

        if commandIntegerCode == 11:
            return self.viewAssistantAssignments(argumentList[0])

        if commandIntegerCode == 12:
            return self.viewContactInfo(argumentList[0])
