from django.test import Client, TestCase
from myApp.models import USER, COURSE


class EditCourseTest(TestCase):

    def setUp(self):
        self.user = USER.objects.create(permission=[1], username="john", password="test", email="john@this.com",
                                        firstName="john", lastName="flupper", contactPhone="2628889765",
                                        officePhone="2624235436", extension="151")
        self.user.save()

        self.course = COURSE.objects.create(name="Intro to CS", courseNumber='150', classNumber='001',
                                            time="MWF 11-11:50", location="EMS 150")

        self.c = Client()
        session = self.c.session
        session['userid'] = self.user.id
        session.save()

    def test_editCourseSelect_get(self):
        ret = self.c.get('/editCourseSelect/')
        self.assertTrue(ret.content.__contains__(b'<title>Select Course</title>'))

    def test_editCourseSelect_post(self):
        ret = self.c.post('/editCourseSelect/', {'userid': 2}, follow=True)
        self.assertTrue(ret.content.__contains__(b'<title>Edit Course Data</title>'))
        self.assertEqual(self.userToEdit.id, self.c.session['editID'])

    def test_editCourse_get(self):
        ret = self.c.get('/editCourse/')
        self.assertTrue(ret.content.__contains__(b'<title>Edit Course</title>'))

    def test_editCourse_fields_1(self):
        ret = self.c.get('/editCourse/')
        self.assertTrue(ret.content.__contains__(b'name="coursename"'))

    def test_editCourse_fields_2(self):
        ret = self.c.get('/editCourse/')
        self.assertTrue(ret.content.__contains__(b'name="coursenumber"'))

    def test_editCourse_fields_3(self):
        ret = self.c.get('/editCourse/')
        self.assertTrue(ret.content.__contains__(b'name="classnumber"'))

    def test_editCourse_fields_4(self):
        ret = self.c.get('/editCourse/')
        self.assertTrue(ret.content.__contains__(b'name="time"'))

    def test_editCourse_fields_5(self):
        ret = self.c.get('/editCourse/')
        self.assertTrue(ret.content.__contains__(b'name="location"'))

    def test_editCourse_fields_6(self):
        ret = self.c.get('/editCourse/')
        self.assertTrue(ret.content.__contains__(b'type="submit"'))
        self.assertTrue(ret.content.__contains__(b'value="Apply"'))

    def test_editCourse_post(self):
        ret = self.c.post('/editCourse/',
                          {'coursename': "CS Principles", 'coursenumber': "101", 'classnumber': "002",
                           'time': "MW 2:00-2:50", 'location': "Lubar S263"}, follow=True)

        self.assertEqual(ret.redirect_chain, [("/commands/", 302)])
        self.assertTrue(ret.content.__contains__(b'<title>Commands</title>'))
        self.assertEqual(self.course.coursename, 'CS Principles')
        self.assertEqual(self.course.coursenumber, '101')
        self.assertEqual(self.course.classnumber, '002')
        self.assertEqual(self.course.time, 'MW 2:00-2:50')
        self.assertEqual(self.course.location, 'Lubar S263')

    # def test_editCourse_error(self):
    #     ret = self.c.post('/editcourse/',
    #                       {'coursename': "CS Principles", 'coursenumber': "101", 'classnumber': "002",
    #                        'time': "MW 2:00-2:50", 'location': "Lubar S263"}, follow=True)

    #     self.assertEqual(ret.status_code, 200)
    #     self.assertTrue(ret.content.__contains__(b'<title>Failed to edit!</title>'))
    #     self.assertTrue(ret.content.__contains__(b'href="http://127.0.0.1:8000/editcourse/"'))
