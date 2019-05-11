from django.test import Client, TestCase
from myApp.models import USER


class logoutHttpTest(TestCase):

    def setUp(self):
        self.user = USER.objects.create(permission=[4], username="john", password="test", email="john@this.com",
                                        firstName="john", lastName="flupper", contactPhone="2628889765",
                                        officePhone="2624235436", extension="151")
        self.user.save()
        self.c = Client()
        session = self.c.session
        session['userid'] = self.user.id
        session.save()

    def testGetLogout(self):
        ret = self.c.get('/logout/')
        self.assertTrue(ret.content.__contains__(b'<title>Log Out</title>'))

    def testPostAffirmLogout(self):
        ret = self.c.post('/logout/', {'Yes'}, follow=True)
        self.assertEqual(ret.redirect_chain, [("/login/", 302)])

    def testPostCancelLogout(self):
        ret = self.c.post('/logout/', {'Cancel'}, follow=True)
        self.assertEqual(ret.redirect_chain, [("/commands/", 302)])

    def test_submit_affirm(self):
        ret = self.c.get('/logout/')
        self.assertTrue(ret.content.__contains__(b'type="submit"'))
        self.assertTrue(ret.content.__contains__(b'value="Log out"'))

    def test_submit_cancel(self):
        ret = self.c.get('/logout/')
        self.assertTrue(ret.content.__contains__(b'type="submit"'))
        self.assertTrue(ret.content.__contains__(b'value="Cancel"'))
