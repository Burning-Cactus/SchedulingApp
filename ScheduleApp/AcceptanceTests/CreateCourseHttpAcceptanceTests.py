from django.test import Client
from django.test import TestCase
from myApp.models import USER


class CreateCourseTest(TestCase):

    def setUp(self):
        self.user = USER.objects.create(permission=[1], username="john", password="test", email="john@this.com",
                                        firstName="john", lastName="flupper", contactPhone="2628889765",
                                        officePhone="2624235436", extension="151")
        self.user.save()

        self.c = Client()
        session = self.c.session
        session['userid'] = self.user.id
        session.save()

    def testCreateCourseGet(self):
        ret = self.c.get('/createCourse/')
        self.assertTrue(ret.content.__contains__(b'<title>Create Course</title>'))

    def testFormMethodAction(self):
        ret = self.c.get('/createCourse/')
        self.assertTrue(ret.content.__contains__(b'<form method="post" action="/createCourse/">'))

    def testFormFields1(self):
        ret = self.c.get('/createCourse/')
        self.assertTrue(ret.content.__contains__(b'name="name"'))

    def testFormFields2(self):
        ret = self.c.get('/createCourse/')
        self.assertTrue(ret.content.__contains__(b'name="classNumber"'))

    def testFormFields3(self):
        ret = self.c.get('/createCourse/')
        self.assertTrue(ret.content.__contains__(b'name="time"'))

    def testFormFields4(self):
        ret = self.c.get('/createCourse/')
        self.assertTrue(ret.content.__contains__(b'name="location"'))

    def testCreateCoursePost(self):
        ret = self.c.post('/createCourse/', {'name': 'physics', 'classNumber': '102', 'time': '3:00am-4:00am',
                                             'location': 'townhall'})

        self.assertEqual(ret.status_code, 302)
        self.assertTrue(ret.content.__contains__(b'<title>Course Created</title>'))
        self.assertTrue(ret.content.__contains__(b'href="http://127.0.0.1:8000/home/"'))

    def testCreateCoursePostError1(self):
        ret = self.c.post('/createCourse/', {'name': '', 'classNumber': '102', 'time': '3:00am-4:00am',
                                             'location': 'townhall'})
        self.assertTrue(ret.content.__contains__(b'<title>Create Course Error</title>'))
        self.assertTrue(ret.content.__contains__(b'href="http://127.0.0.1:8000/createCourse/"'))

    def testCreateCoursePostError2(self):
        ret = self.c.post('/createCourse/', {'name': 'physics', 'classNumber': '', 'time': '3:00am-4:00am',
                                             'location': 'townhall'})
        self.assertTrue(ret.content.__contains__(b'<title>Create Course Error</title>'))
        self.assertTrue(ret.content.__contains__(b'href="http://127.0.0.1:8000/createCourse/"'))

    def testCreateCoursePostError3(self):
        ret = self.c.post('/createCourse/', {'name': 'physics', 'classNumber': '102', 'time': '',
                                             'location': 'townhall'})
        self.assertTrue(ret.content.__contains__(b'<title>Create Course Error</title>'))
        self.assertTrue(ret.content.__contains__(b'href="http://127.0.0.1:8000/createCourse/"'))

    def testCreateCoursePostError4(self):
        ret = self.c.post('/createCourse/', {'name': 'physics', 'classNumber': '102', 'time': '3:00am-4:00am',
                                             'location': ''})
        self.assertTrue(ret.content.__contains__(b'<title>Create Course Error</title>'))
        self.assertTrue(ret.content.__contains__(b'href="http://127.0.0.1:8000/createCourse/"'))
