from django.test import Client
from django.test import TestCase
from myApp.models import USER


class AccessDataTests(TestCase):

    def setUp(self):
        self.user = USER.objects.create(permission=[1], username="semor", password="test", email="luper@this.com",
                                        firstName="semor", lastName="flupper", contactPhone="2628889765",
                                        officePhone="2624235436", extension="151")

        self.user.save()
        self.c = Client()
        session = self.c.session
        session['userid'] = self.user.id
        session.save()




    def testAccessDataGet1(self):
        with self.assertTemplateUsed('shell/accessAllData.html'):
            ret = self.c.get('/accessAllData/')
        self.assertTrue(ret.content.__contains__(b'<title>Data</title>'))

    def testAccessDataGet2(self):
        ret = self.c.get('/accessAllData/')
        self.assertTrue(ret.content.__contains__(b'User:'))

    def testAccessDataGet3(self):
        ret = self.c.get('/accessAllData/')
        self.assertTrue(ret.content.__contains__(b'Courses:'))

    def testAccessDataGet4(self):
        ret = self.c.get('/accessAllData/')
        self.assertTrue(ret.content.__contains__(b'Assistant Assignments:'))

    def testAccessDataGet5(self):
        ret = self.c.get('/accessAllData/')
        self.assertTrue(ret.content.__contains__(b'Instructor Assignments:'))

    def testAccessDataGet6(self):
        ret = self.c.get('/accessAllData/')
        self.assertTrue(ret.content.__contains__(b'Labs:'))

    def test_AccessData_Table(self):
        ret = self.c.get('/accessAllData/')
        self.assertTrue(ret.content.__contains__(b'<table'))


