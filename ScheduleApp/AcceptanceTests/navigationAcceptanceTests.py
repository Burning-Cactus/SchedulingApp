from django.test import Client, TestCase
from myApp.models import USER


class loginHttpAcceptanceTests(TestCase):

    def setUp(self):
        self.user = USER.objects.create(permission=[4], username="john", password="test", email="john@this.com",
                                        firstName="john", lastName="flupper", contactPhone="2628889765",
                                        officePhone="2624235436", extension="151")

        self.user.save()

    def testSupervisorNavigation(self, url, permission):
        self.setupSession(permission)
        ret = self.c.get(url)
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/createAccount/'))
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/createCourse/'))
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/createLab/'))
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/editSelect/'))
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/editCourse/'))
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/editLab/'))
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/assignAssistantToLab/'))
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/assignInstructorToCourse/'))
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/assignAssistantToCourse/'))
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/accessAllData/'))
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/deleteSelect/'))
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/deleteLab/'))
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/deleteCourse/'))
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/logout/'))
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/email/'))

    def testAdministratorNavigation(self, url, permission):
        self.setupSession(permission)
        ret = self.c.get(url)
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/createAccount/'))
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/createCourse/'))
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/createLab/'))
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/editAccount/'))
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/accessAllData/'))
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/deleteSelect/'))
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/logout/'))
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/email/'))

    def testInstructorNavigation(self, url, permission):
        self.setupSession(permission)
        ret = self.c.get(url)
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/editContactInfo/'))
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/viewCourseAssignments/'))
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/viewAssistantAssignments/'))
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/assignAssistantToLab/'))
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/viewPublicContactInfo/'))
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/logout/'))
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/email/'))

    def testAssistantNavigation(self, url, permission):
        self.setupSession(permission)
        ret = self.c.get(url)
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/editContactInfo/'))
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/viewAssistantAssignments/'))
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/viewPublicContactInfo/'))
        self.assertTrue(ret.content.__contains__(b'href=http://127.0.0.1:8000/logout/'))

    def setupSession(self, permission):
        self.c = Client()
        self.user.permission = permission
        session = self.c.session
        session['userid'] = self.user.id
        session.save()