from django.db import models

# Create your models here.


class USER(models.Model):
    pass


class LAB_SECTION(models.Model):
    pass


class A_LIST(models.Model):
    pass


class COURSE(models.Model):
    pass


class I_LIST(models.Model):
    pass


class Terminal:

    def command(self, inStr):
        return inStr

    def login(self):
        return

    def logout(self):
        return

    def createAccount(self):
        return""

    def editAccount(self):
        return""

    def deleteAccount(self):
        return""

    def createCourse(self):
        return""

    def email(self):
        return""

    def accessData(self):
        return""

    def assignInstructorToCourse(self):
        return""

    def assignAssistantToCourse(self):
        return""

    def viewCourseAssignments(self):
        return""

    def viewAssistantAssignments(self):
        return""

    def viewContactInfo(self):
        return""
    # pass
