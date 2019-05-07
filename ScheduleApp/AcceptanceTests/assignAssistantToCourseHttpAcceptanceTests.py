from django.test import Client
from django.test import TestCase
from myApp.models import USER


class AssignAssistantToCourseTest(TestCase):

    def setUp(self):
        self.user = USER.objects.create(permission=[1], username="john", password="test", email="john@this.com",
                                        firstName="john", lastName="flupper", contactPhone="2628889765",
                                        officePhone="2624235436", extension="151")
        self.user.save()

        self.c = Client()
        session = self.c.session
        session['userid'] = self.user.id
        session.save()

    def testAssignAssistantToCoursetGet(self):
        ret = self.c.get('/assignAssistantToCourse/')
        self.assertTrue(ret.content.__contains__(b'<title>Assign Assistant To Course</title>'))

    def testFormMethodAction(self):
        ret = self.c.get('/assignAssistantToCourse/')
        self.assertTrue(ret.content.__contains__(b'<form method="post"'))
        self.assertTrue(ret.content.__contains__(b'action="/assignAssistantToCourse/">'))

    def testFormFields(self):
        ret = self.c.get('/assignAssistantToCourse/')
        self.assertTrue(ret.content.__contains__(b'name="userId"'))
        self.assertTrue(ret.content.__contains__(b'name="courseId"'))

    def testAssignAssistantToCoursePost(self):
        user = USER.objects.create(permission=[1], username="pablo", password="test", email="john@this.com",
                                        firstName="john", lastName="flupper", contactPhone="2628889765",
                                        officePhone="2624235436", extension="151")
        ret = self.c.post('/assignAssistantToCourse/',
                          {'couseid': '1', 'assastantid': user.get('''userId''')}, follow=True)#P.S '''userId''' is a placeholder for actually getting the Id forgot how to acces hidden spooky feild
        self.assertEqual(ret.status_code, 200)
        self.assertTrue(ret.content.__contains__(b'href="http://127.0.0.1:8000/shell/commands/"'))

    def testAssignAssistantToCoursePostError(self):
        ret = self.c.post('/assignAssistantToCourse/',
                          {'couseid': '1', 'assastantid': '0'}, follow=True)
        self.assertEqual(ret.status_code, 302)
        self.assertTrue(ret.content.__contains__(b'href="http://127.0.0.1:8000/assignAssistantToCourseError/"'))

    def testNumberFourm(self):
        ret = self.c.get('/assignAssistantToCourse/')
        self.assertTrue(ret.content.__contains__(b'type="number"'))

    def testSubmitButton(self):
        ret = self.c.get('/assignAssistantToCourse/')
        self.assertTrue(ret.content.__contains__(b'type="Assign Assistant"'))