from django.test import Client, TestCase
from myApp.models import USER, COURSE


# Andy
class DeleteAccountHttpAcceptanceTest(TestCase):

    def setUp(self):
        self.userToDelete.save()
        self.course = COURSE.objects.create(name="Intro to CS TEST", courseNumber='150', classNumber='001',
                                            time="MWF 11-11:50", location="EMS 150")
        self.course.save()
        self.c = Client()
        session = self.c.session
        session['userid'] = self.user.id
        session.save()

    # HTML Tests
        # deleteCourse.html 's tests
    # Post method redirect test
    def testDeleteCoursePost(self):
        ret = self.c.post('/deleteCourse/',
                          {'courseid': self.c.session[USER.objects.get(name="Intro to CS TEST")]}, follow=True)

        self.assertEqual(ret.redirect_chain, [("/commands/", 302)])

    # HTML file tests
    def testFormMethodAction(self):
        ret = self.c.get('/deleteCourse/')
        self.assertTrue(ret.content.__contains__(b'<form method="post", action="http://127.0.0.1:8000/commands/">'))

    def testSubmit(self):
        ret = self.c.get('/deleteCourse/')
        self.assertTrue(ret.content.__contains__(b'type="submit"'))
        self.assertTrue(ret.content.__contains__(b'value="Submit"'))

    # Functionality Tests
    # Tests for deletion being done
    def testDeleteCourse(self):
        self.setUp()
        course_to_delete = self.c.session[COURSE.objects.get(name="Intro to CS TEST")]

        # Go to the delete the course
        ro = self.c.post('deleteCourse.html', {'courseid': course_to_delete})

        # Make sure we redirect to the proper page for deleting
        url = ro.redirect_chain
        self.assertEquals(url, ['http://127.0.0.1:8000/commands'])

        # Check to ensure that the user is gone
        self.assertEqual(self.c.session['name'], None)
