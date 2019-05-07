from django.test import Client
from django.test import TestCase
from myApp.models import USER, I_LIST, COURSE

class viewCourseAssignmentsHttpAcceptanceTests(TestCase):

    def setUp(self):
        self.user = USER.objects.create(permission='13', username="john", password="test", email="john@this.com",
                                        firstName="john", lastName="flupper", contactPhone="2628889765",
                                        officePhone="2624235436", extension="151")
        self.course = COURSE.objects.create(name='Compsci', courseNumber='125', classNumber='026', time='20:20', location='viva')
        self.Ilist = I_LIST.objects.create(instructorID=self.user.id, courseID=self.course.id)
        self.user.save()
        self.c = Client()
        session = self.c.session
        session['userid'] = self.user.id
        session.save()

    def testVCAGet(self):
        self.c = Client()
        response = self.c.get('/viewCourseAssignments/')
        self.assertTrue(response.content.__contains__(b'<title>Assigned Courses<title>'))

    def testDisplay(self):
        with self.assertTemplateUsed('shell/viewCourseAssignments.html'):
            response = self.c.get('/viewCourseAssignments/')
            # response.context['Instructor'] == [self.firstName]
            # response.context['Course'] == [self.course.name + ' ' + self.course.courseNumber]

