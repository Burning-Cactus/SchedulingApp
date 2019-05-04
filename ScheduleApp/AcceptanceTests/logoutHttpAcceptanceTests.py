from django.test import Client, TestCase
from myApp.models import USER


class logoutHttpTest(TestCase):

    def setUp(self):
        self.user = USER.objects.create(permission=[4], username="john", password="test", email="john@this.com",
                                        firstName="john", lastName="flupper", contactPhone="2628889765",
                                        officePhone="2624235436", extension="151")
        self.c = Client()

    def testGetLogout(self):
        ret = self.c.get('/logout/')
        self.assertTrue(ret.content.__contains__(b'<title>Log Out</title>'))

    def testPostAffirmLogout(self):
        ret = self.c.post('/logout/', {'Yes'}, follow=True)
        self.assertEqual(ret.redirect_chain, [("/login/", 302)])

    def testPostCancelLogout(self):
        ret = self.c.post('/logout/', {'Cancel'}, follow=True)
        self.assertEqual(ret.redirect_chain, [("/commands/", 302)])
