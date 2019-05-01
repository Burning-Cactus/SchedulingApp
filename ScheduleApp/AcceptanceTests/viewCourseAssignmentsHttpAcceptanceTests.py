from django.test import Client
from django.test import TestCase
from myApp.models import USER

class viewCourseAssignmentsHttpAcceptanceTests(TestCase):

    def setup(self):
        self.user = USER.objects.create(permission=[1], username="john", password="test", email="john@this.com",
                                        firstName="john", lastName="flupper", contactPhone="2628889765",
                                        officePhone="2624235436", extension="151")
        self.c = Client()
        session = self.c.session
        session['userid'] = self.user.id
        session.save()

    def testVCAGet(self):
        self.c = Client()
        response = self.c.get('/viewCourseAssignments/')
        self.assertTrue(response.content.__contains__(b'<title>Assigned Courses<title>'))

    def testVCAGet2(self):
        self.c = Client()
        response = self.c.get('/viewCourseAssignments/')
        self.assertTrue(response.content.__contains__(b'USER'))

    def testVCAGet3(self):
        self.c = Client()
        response = self.c.get('/viewCourseAssignments/')
        self.assertTrue(response.content.__contains__(b'I_LIST'))