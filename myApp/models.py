from django.db import models
from ScheduleApp import User, Course

# Create your models here.


class USER(models.Model):
    username = models.CharField(max_length = 60)
    password = models.CharField(max_length = 60)
    permission = models.CharField(max_length = 5)
    email = models.CharField(max_length = 60)
    firstname = models.CharField(max_length = 60)
    lastname = models.CharField(max_length = 60)
    contactphone = models.CharField(max_length = 12)
    extension = models.CharField(max_length = 5)


class LAB_SECTION(models.Model):
    pass


class A_LIST(models.Model):
    pass


class COURSE(models.Model):
    name = models.CharField(max_length = 60)
    courseNumber = models.CharField(max_length = 60)
    classNumber = models.CharField(max_length = 60)
    labList = models.CharField(max_length = 60)
    time = models.CharField(max_length = 60)
    location = models.CharField(max_length = 60)
    pass


class I_LIST(models.Model):
    pass


class Terminal:
    # This class will be used to execute commands with the database.

    def command(self, inStr):
        return inStr

    def login(self, xName, xPassword):
        # Create and return a user object from the database after checking the username and password
        person = User()
        return person

    def logout(self, xUser):
        # Destroy the user object currently being used
        return

    def createAccount(self, first, last, username, password, email, permission):
        # Create a new user in the database with all of the parameters provided and a generated ID.
        person = User()
        person.toString()
        return""

    def editAccount(self, userid):
        # Change the values of a user in the database.
        return""

    def deleteAccount(self, userid):
        # Delete a user model in the database.
        return""

    def createCourse(self, name, coursenumber, classnumber, time, location):
        # Create a course in the database with a generated ID.
        if self.user == Null:
            return "You must be logged in."
        if self.user.permission == 3:
            return "You do not have permissions to use this function."
        if self.user.permission == 4:
            return "You do not have permissions to use this function."
        course = Course()
        course.setName(name)
        course.setCourseNumber(coursenumber)
        course.setClassNumber(classnumber)
        course.setTime(time)
        course.setLocation(location)
        return"Course successfully created."

    def deleteCourse(self, coursenumber, classnumber):
        # Delete a course from the database
        return""

    def email(self, message):
        # Send out an email to notify all recipients.
        return""

    def accessData(self):
        # Access all data in the system and print it in tables
        return""

    def assignInstructorToCourse(self, courseid, instructorid):
        # Assign an instructor to a course in the database
        return""

    def assignAssistantToCourse(self, courseid, instructorid):
        # Assign a TA to a course in the database
        return""

    def viewCourseAssignments(self, userid):
        # Return data on instructor assignments in the database.
        return""

    def viewAssistantAssignments(self, userid):
        # Return data on TA assignments in the database
        return""

    def viewContactInfo(self, userid):
        # Return the contact info of the user.
        return""
    # pass
