from django.test import Client, TestCase
from myApp.models import USER, COURSE


# Andy
class DeleteAccountHttpAcceptanceTest(TestCase):

    def setUp(self):
        self.userToDelete = USER.objects.create(permission=[4], username="john", password="test", email="john@this.com",
                                    firstName="john", lastName="flupper", contactPhone="2628889765",
                                    officePhone="2624235436", extension="151")
        self.userToDelete.save()
        self.course = COURSE.objects.create(name="Intro to CS", courseNumber='150', classNumber='001',
                                            time="MWF 11-11:50", location="EMS 150")

        self.c = Client()
        session = self.c.session
        session['userid'] = self.user.id
        session.save()

    # Functionality Tests
    # Tests for deletion being done
    def testDeleteCourse(self):
        self.setUp()
        idToDelete = self.c.session[USER.objects.get(username="john")]

        # Go to the delete user selection page
        ro = self.c.post('deleteSelect.html', {'userid': idToDelete})

        # Make sure we redirect to the proper page for deleting
        url = ro.redirect_chain
        self.assertEquals(url, ['deleteAccount.html'])

        # delete UserId
        go = self.c.post('deleteAccount.html')

        # after deleted, go home
        url = go.redirect_chain
        self.assertEquals(url, ['http://127.0.0.1:8000/commands'])

        # Check to ensure that the user is gone
        self.assertEqual(self.c.session['userid'], None)

    # HTML Tests
        # deleteSelect.html 's tests
    def testDeleteSelectPost(self):
        with self.assertTemplateUsed("deleteAccount.html"):
            with self.assertTemplateNotUsed("homepage.html"):
                res = self.client.get("/deleteSelect/", follow=True)
                expected_url = "/deleteAccount/"
                self.assertRedirects(res, expected_url)

        # deleteAccount.html 's tests
    def testDeleteAccountGet(self):
        with self.assertTemplateUsed("commands.html"):
            with self.assertTemplateNotUsed("deleteSelect.html"):
                res = self.client.get("/deleteAccount/", follow=True)
                expected_url = "/commands/"
                self.assertRedirects(res, expected_url)

    # HTML file tests
    def testFormMethodAction(self):
        ret = self.c.get('/deleteAccount/')
        self.assertTrue(ret.content.__contains__(b'<form method="post", action="http://127.0.0.1:8000/commands/">'))

    def testSubmit(self):
        ret = self.c.get('/deleteAccount/')
        self.assertTrue(ret.content.__contains__(b'type="submit"'))
        self.assertTrue(ret.content.__contains__(b'value="Submit"'))

    def test_title(self):
        ret = self.c.get('/deleteAccount/')
        self.assertTrue(ret.content.__contains__(b'<title>Delete Account?</title>'))
