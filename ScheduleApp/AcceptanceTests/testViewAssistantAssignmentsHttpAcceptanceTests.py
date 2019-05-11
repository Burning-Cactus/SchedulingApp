from django.test import Client
from django.test import TestCase
from myApp.models import USER

class viewAssistantAssignmentsHttpAcceptanceTests(TestCase):

    def setup(self):
        self.user = USER.objects.create(permission=[1], username="john", password="test", email="john@this.com",
                                        firstName="john", lastName="flupper", contactPhone="2628889765",
                                        officePhone="2624235436", extension="151")
        self.c = Client()
        session = self.c.session
        session['userid'] = self.user.id
        session.save()

    def testVAAGet(self):
        self.c = Client()
        response = self.c.get('/viewAssistantAssignments/')
        self.assertTrue(response.content.__contains__(b'<title>Assigned Assistants<title>'))

    def testVAAGet2(self):
        self.c = Client()
        response = self.c.get('/viewAssistantAssignments/')
        self.assertTrue(response.content.__contains__(b'USER'))

    def testVAAGet3(self):
        self.c = Client()
        response = self.c.get('/viewAssistantAssignments/')
        self.assertTrue(response.content.__contains__(b'A_LIST'))