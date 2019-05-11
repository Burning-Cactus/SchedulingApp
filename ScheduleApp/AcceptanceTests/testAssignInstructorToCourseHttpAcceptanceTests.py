from django.test import Client
from django.test import TestCase
from myApp.models import USER, COURSE


class assignInstuctorToCourseHttpTests(TestCase):

    def setUp(self):
        self.user = USER.objects.create(permission=[1], username="john", password="test", email="john@this.com",
                                        firstName="john", lastName="flupper", contactPhone="2628889765",
                                        officePhone="2624235436", extension="151")
        self.user.save()

        self.course = COURSE.objects.create(name='TestClass', courseNumber='602', classNumber='401', time='9:30 am',
                                            location='Test Hall')
        self.course.save()

        self.c = Client()
        session = self.c.session
        session['userid'] = self.user.id
        session.save()

    def testGetWithUserRedirect(self):
        with self.assertTemplateUsed('assignInstructorToCourse.html'):
            self.c.get('/assignInstructor/', follow=True)

    def testAssignInstructorToCourseTable(self):
        ret = self.c.get('/assignInstructor/')
        self.assertTrue(ret.content.__contains__(b'<table>'))
        self.assertTrue(ret.content.__contains__(b'<tr><th>ID</th><th>Permission</th> <th>User Name</th> '
                                                 b'<th>Password</th> ' b'<th>Email</th> <th>First Name</th> '
                                                 b'<th>Last Name</th> 'b'<th>ContactPhone</th> <th>OfficePhone</th> '
                                                 b'<th>Extension</th></tr>'))
        self.assertTrue(ret.content.__contains__(b'<tr><th>ID</th><th>Name</th> <th>Course Number</th> '
                                                 b'<th>Class Number</th> 'b'<th>time</th> <th>location</th></tr>'))
        self.assertTrue(ret.content.__contains__(b'</table>'))

    def TestAssignInstructorToCourseGet(self):
        ret = self.c.get('/assignInstructor/')
        self.assertTrue(ret.content.__contains__(b'<title>Assign Instructor To Course</title>'))

    def testFormMethodAction(self):
        ret = self.c.get('/assignInstructor/')
        self.assertTrue(
            ret.content.__contains__(b'<form method="post" action="/assignInstructor/">'))

    #def testFormFields1(self):
    #    ret = self.c.get('/assignInstructor/')
    #    self.assertTrue(ret.content.__contains__(b'name="instructorID"'))

    #def testFormFields2(self):
    #    ret = self.c.get('/assignInstructor/')
    #    self.assertTrue(ret.content.__contains__(b'name="courseID"'))

    def testSubmit(self):
        ret = self.c.get('/assignInstructor/')
        self.assertTrue(ret.content.__contains__(b'type="submit"'))
        self.assertTrue(ret.content.__contains__(b'value="Assign Instructor to Course"'))

    def testTypes1(self):
        ret = self.c.get('/assignInstructor/')
        self.assertTrue(ret.content.__contains__(b'type="submit"'))

    def testTypes3(self):
        ret = self.c.get('/assignInstructor/')
        self.assertTrue(ret.content.__contains__(b'type="number"'))
