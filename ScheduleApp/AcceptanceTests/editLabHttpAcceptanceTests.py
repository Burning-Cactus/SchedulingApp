from django.test import Client
from django.test import TestCase
from myApp.models import USER, LAB_SECTION, COURSE


class EditLabTests(TestCase):

    def setup(self):
        self.user = USER.objects.create(permission=[1], username="john", password="test", email="john@this.com",
                                        firstName="john", lastName="flupper", contactPhone="2628889765",
                                        officePhone="2624235436", extension="151")
        self.user.save()

        self.course = COURSE.objects.create(name='TestClass', courseNumber='602', classNumber='401', time='9:30 am',
                                            location='Test Hall')
        self.course.save()

        self.lab = LAB_SECTION.objects.create(name='TestLab', labNumber='602', courseID=self.course.id, time='9:30 am'
                                              , location='Test Hall')
        self.lab.save()

        self.c = Client()
        session = self.c.session
        session['userid'] = self.user.id
        session.save()

    def testGetWithUserRedirect(self):
        with self.assertTemplateUsed('editLab.html'):
            self.c.get('/editLab/', follow=True)

    def TestEditLabGet(self):
        ret = self.c.get('/editLab/')
        self.assertTrue(ret.content.__contains__(b'<title>Edit Lab</title>'))

    def testFormMethodAction(self):
        ret = self.c.get('/editLab/')
        self.assertTrue(
            ret.content.__contains__(b'<form method="post" action="/editLab/">'))

    def testFormFields1(self):
        ret = self.c.get('/editLab/')
        self.assertTrue(ret.content.__contains__(b'name="labName"'))

    def testFormFields2(self):
        ret = self.c.get('/editLab/')
        self.assertTrue(ret.content.__contains__(b'name="labNumber"'))

    def testFormFields3(self):
        ret = self.c.get('/editLab/')
        self.assertTrue(ret.content.__contains__(b'name="courseId"'))

    def testFormFields4(self):
        ret = self.c.get('/editLab/')
        self.assertTrue(ret.content.__contains__(b'name="time"'))

    def testFormFields5(self):
        ret = self.c.get('/editLab/')
        self.assertTrue(ret.content.__contains__(b'name="location"'))

    def testSubmit(self):
        ret = self.c.get('/editLab/')
        self.assertTrue(ret.content.__contains__(b'type="submit"'))
        self.assertTrue(ret.content.__contains__(b'value="Edit Lab"'))

    def testTypes1(self):
        ret = self.c.get('/editLab/')
        self.assertTrue(ret.content.__contains__(b'type="submit"'))

    def testTypes2(self):
        ret = self.c.get('/editLab/')
        self.assertTrue(ret.content.__contains__(b'type="str"'))

    def testTypes3(self):
        ret = self.c.get('/editLab/')
        self.assertTrue(ret.content.__contains__(b'type="number"'))

    def testTypes4(self):
        ret = self.c.get('/editLab/')
        self.assertTrue(ret.content.__contains__(b'type="time"'))


