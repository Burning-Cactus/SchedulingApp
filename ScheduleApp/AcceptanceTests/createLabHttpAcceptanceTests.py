from django.test import Client
from django.test import TestCase
from myApp.models import USER, LAB_SECTION


class CreateLabTests(TestCase):

    def setup(self):
        self.user = USER.objects.create(permission=[1], username="john", password="test", email="john@this.com",
                                        firstName="john", lastName="flupper", contactPhone="2628889765",
                                        officePhone="2624235436", extension="151")
        self.user.save()

        self.lab = LAB_SECTION.objects.create('/createCourse/', {'name': 'TestClass', 'courseNumber': '602', 'classNumber': '401',
                                             'time': '9:30 am', 'location': 'Test Hall'})

        self.c = Client()
        session = self.c.session
        session['userid'] = self.user.id
        session.save()

    def TestCreateLabGet(self):
        ret = self.c.get('/createLab/')
        self.assertTrue(ret.content.__contains__(b'<title>Create Lab</title>'))

    def testFormMethodAction(self):
        ret = self.c.get('/createLab/')
        self.assertTrue(
            ret.content.__contains__(b'<form method="post" action="/createLab/">'))

    def testFormFields1(self):
        ret = self.c.get('/createLab/')
        self.assertTrue(ret.content.__contains__(b'name="labName"'))

    def testFormFields2(self):
        ret = self.c.get('/createLab/')
        self.assertTrue(ret.content.__contains__(b'name="labNumber"'))

    def testFormFields3(self):
        ret = self.c.get('/createLab/')
        self.assertTrue(ret.content.__contains__(b'name="courseId"'))

    def testFormFields4(self):
        ret = self.c.get('/createLab/')
        self.assertTrue(ret.content.__contains__(b'name="time"'))

    def testFormFields5(self):
        ret = self.c.get('/createLab/')
        self.assertTrue(ret.content.__contains__(b'name="location"'))

    def testSubmit(self):
        ret = self.c.get('/createLab/')
        self.assertTrue(ret.content.__contains__(b'type="submit"'))
        self.assertTrue(ret.content.__contains__(b'value="Create Lab"'))

    def testCreateLabPost(self):
        ret = self.c.post('/createLab/', {'name': 'Test Lab', 'labNumber': '500', 'courseID': self.lab,
                                          'time': '11:00 am', 'location': 'Test Hall'})
        self.assertEqual(ret.status_code, 302)
        self.assertTrue(ret.conent.__contains__(b'<title>Lab Created</title>'))
        self.assertTrue(ret.conent.__contains__(b'href="/home/"'))

    def testCreateLabPostError1(self):
        ret = self.c.post('/createLab/', {'name': '', 'labNumber': '500', 'courseID': self.lab,
                                          'time': '11:00 am', 'location': 'Test Hall'})

        self.assertTrue(ret.conent.__contains__(b'<title>Create Lab Error</title>'))
        self.assertTrue(ret.conent.__contains__(b'href="/createLab/"'))

    def testCreateLabPostError2(self):
        ret = self.c.post('/createLab/', {'name': 'Test Lab', 'labNumber': '', 'courseID': self.lab,
                                          'time': '11:00 am', 'location': 'Test Hall'})

        self.assertTrue(ret.conent.__contains__(b'<title>Create Lab Error</title>'))
        self.assertTrue(ret.conent.__contains__(b'href="/createLab/"'))