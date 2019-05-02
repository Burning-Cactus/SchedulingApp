from django.test import Client, TestCase
from myApp.models import USER, COURSE


class EditCourseTest(TestCase):

    def setup(self):
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

    def test_editCourse_get(self):
        ret = self.c.get('/editcourse/')
        self.assertTrue(ret.content.__contains__(b'<title>Edit Course</title>'))

    def test_editCourse_fields(self):
        ret = self.c.get('/editcourse/')
        self.assertTrue(ret.content.__contains__(b'name="coursename"'))
        self.assertTrue(ret.content.__contains__(b'name="coursenumber"'))
        self.assertTrue(ret.content.__contains__(b'name="classnumber"'))
        self.assertTrue(ret.content.__contains__(b'name="time"'))
        self.assertTrue(ret.content.__contains__(b'name="location"'))
        self.assertTrue(ret.content.__contains__(b'type="submit"'))
        self.assertTrue(ret.content.__contains__(b'value="Apply"'))

    def test_editCourse_post(self):

        pass

    def test_editCourse_error(self):
        ret = self.c.post('/editcourse/',
                          {'coursename': "CS Principles", 'coursenumber': "101", 'classnumber': "002",
                           'time': "MW 2:00-2:50", 'location': "Lubar S263"})

        self.assertEqual(ret.status_code, 200)
        self.assertTrue(ret.content.__contains__(b'<title>Failed to edit!</title>'))
        self.assertTrue(ret.content.__contains__(b'href="http://127.0.0.1:8000/editcourse/"'))
