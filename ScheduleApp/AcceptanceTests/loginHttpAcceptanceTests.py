from django.test import Client, TestCase
from myApp.models import USER


class loginHttpAcceptanceTests(TestCase):

    def setUp(self):
        self.user = USER.objects.create(permission=[4], username="john", password="test", email="john@this.com",
                                        firstName="john", lastName="flupper", contactPhone="2628889765",
                                        officePhone="2624235436", extension="151")

        self.c = Client()


    def testGetLogin(self):
        with self.assertTemplateUsed('shell/login.html'):
            ret = self.c.get('/login/')
        self.assertTrue(ret.content.__contains__(b'<title>Log In</title>'))


    def testLoginPost(self):

        ret = self.c.post('/login/', {'UserName': self.user.username, 'Password': self.user.password}, follow=True)
        self.assertEqual(ret.redirect_chain, [("/commands/", 302)])

        userId = self.c.session['userid']
        self.assertEqual(userId, self.user.id)

    def testLoginPostError1(self):

        ret = self.c.post('/login/', {'UserName': '', 'Password': self.user.password})
        self.assertEqual(ret.content.__contains__(b'<tile>Login Error</title>'))

    def testLoginPostError2(self):

        ret = self.c.post('/login/', {'UserName': '', 'Password': ''})
        self.assertEqual(ret.content.__contains__(b'<tile>Login Error</title>'))

    def testLoginPostError3(self):

        ret = self.c.post('/login/', {'UserName': self.user.username, 'Password': ''})
        self.assertEqual(ret.content.__contains__(b'<tile>Login Error</title>'))






