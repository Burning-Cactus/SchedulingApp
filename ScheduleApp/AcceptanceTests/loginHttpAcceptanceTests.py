from django.test import Client, TestCase
from myApp.models import USER


class loginHttpAcceptanceTests(TestCase):

    def setUp(self):
        self.user = USER.objects.create(permission=[4], username="john", password="test", email="john@this.com",
                                        firstName="john", lastName="flupper", contactPhone="2628889765",
                                        officePhone="2624235436", extension="151")



    def testLoginSuccess(self):

        c = Client()

        ret = c.post('/login/', {'username': self.user.username, 'password': self.user.password})
        url = ret.redirect_chain
        self.assertEquals(url, [('http://127.0.0.1:8000/home', 302)])

        userId = c.session['userid']
        self.assertEqual(userId, self.user.id)





