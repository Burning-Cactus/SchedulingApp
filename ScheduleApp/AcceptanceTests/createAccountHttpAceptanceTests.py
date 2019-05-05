from django.test import Client
from django.test import TestCase
from myApp.models import USER


class CreateAccountTest(TestCase):

    def setUp(self):
        self.user = USER.objects.create(permission=[1], username="john", password="test", email="john@this.com",
                                        firstName="john", lastName="flupper", contactPhone="2628889765",
                                        officePhone="2624235436", extension="151")
        self.user.save()

        self.c = Client()
        session = self.c.session
        session['userid'] = self.user.id
        session.save()

    def testCreateAccountGet(self):
        ret = self.c.get('/createAccount/')
        self.assertTrue(ret.content.__contains__(b'<title>Create Account</title>'))

    def testFormMethodAction(self):
        ret = self.c.get('/createAccount/')
        self.assertTrue(ret.content.__contains__(b'<form method="post"'))
        self.assertTrue(ret.content.__contains__(b'action="/createAccount/">'))

    def testFormFields(self):
        ret = self.c.get('/createAccount/')
        self.assertTrue(ret.content.__contains__(b'name="permission"'))
        self.assertTrue(ret.content.__contains__(b'name="username"'))
        self.assertTrue(ret.content.__contains__(b'name="password"'))
        self.assertTrue(ret.content.__contains__(b'name="email"'))
        self.assertTrue(ret.content.__contains__(b'name="firstName"'))
        self.assertTrue(ret.content.__contains__(b'name="lastName"'))
        self.assertTrue(ret.content.__contains__(b'name="contactPhone"'))
        self.assertTrue(ret.content.__contains__(b'name="officePhone"'))
        self.assertTrue(ret.content.__contains__(b'name="extension"'))
        self.assertTrue(ret.content.__contains__(b'type="submit"'))
        self.assertTrue(ret.content.__contains__(b'value="Create"'))

    def testCreateAccountPost(self):
        ret = self.c.post('/createAccount/', {'username': 'jim', 'password': 'wild', 'permission': '[1]', 'email': 'jim@this.com',
                                               'firstName': 'jim', 'lastName': 'halpert', 'contactPhone': '111-111-1111',
                                               'officePhone': '111-111-1111', 'extension': '111'}, follow=True)

        self.assertEqual(ret.status_code, 200)
        self.assertTrue(ret.content.__contains__(b'href="http://127.0.0.1:8000/shell/commands/"'))

    def testCreateAccountPostError1(self):
        ret = self.c.post('/createAccount/',
                          {'username': '', 'password': 'wild', 'permission': '[1]', 'email': 'jim@this.com',
                           'firstName': 'jim', 'lastName': 'halpert', 'contactPhone': '111-111-1111',
                           'officePhone': '111-111-1111', 'extension': '111'}, follow=True)

        self.assertEqual(ret.status_code, 302)
        self.assertTrue(ret.content.__contains__(b'href="http://127.0.0.1:8000/createAccountError/"'))

    def testCreateAccountPostError3(self):
        ret = self.c.post('/createAccount/',
                          {'username': 'jim', 'password': '', 'permission': '[1]', 'email': 'jim@this.com',
                           'firstName': 'jim', 'lastName': 'halpert', 'contactPhone': '111-111-1111',
                           'officePhone': '111-111-1111', 'extension': '111'}, follow=True)

        self.assertEqual(ret.status_code, 302)
        self.assertTrue(ret.content.__contains__(b'href="http://127.0.0.1:8000/createAccountError/"'))

    def testCreateAccountPostError4(self):
        ret = self.c.post('/createAccount/',
                          {'username': 'jim', 'password': 'wild', 'permission': '', 'email': 'jim@this.com',
                           'firstName': 'jim', 'lastName': 'halpert', 'contactPhone': '111-111-1111',
                           'officePhone': '111-111-1111', 'extension': '111'}, follow=True)

        self.assertEqual(ret.status_code, 302)
        self.assertTrue(ret.content.__contains__(b'href="http://127.0.0.1:8000/createAccountError/"'))

    def testCreateAccountPostError5(self):
        ret = self.c.post('/createAccount/',
                          {'username': 'jim', 'password': 'wild', 'permission': '[1]', 'email': '',
                           'firstName': 'jim', 'lastName': 'halpert', 'contactPhone': '111-111-1111',
                           'officePhone': '111-111-1111', 'extension': '111'}, follow=True)

        self.assertEqual(ret.status_code, 302)
        self.assertTrue(ret.content.__contains__(b'href="http://127.0.0.1:8000/createAccountError/"'))

    def testCreateAccountPostError6(self):
        ret = self.c.post('/createAccount/',
                          {'username': 'jim', 'password': 'wild', 'permission': '[1]', 'email': 'jim@this.com',
                           'firstName': '', 'lastName': 'halpert', 'contactPhone': '111-111-1111',
                           'officePhone': '111-111-1111', 'extension': '111'}, follow=True)

        self.assertEqual(ret.status_code, 302)
        self.assertTrue(ret.content.__contains__(b'href="http://127.0.0.1:8000/createAccountError/"'))

    def testCreateAccountPostError7(self):
        ret = self.c.post('/createAccount/',
                          {'username': 'jim', 'password': 'wild', 'permission': '[1]', 'email': 'jim@this.com',
                           'firstName': 'jim', 'lastName': '', 'contactPhone': '111-111-1111',
                           'officePhone': '111-111-1111', 'extension': '111'}, follow=True)

        self.assertEqual(ret.status_code, 302)
        self.assertTrue(ret.content.__contains__(b'href="http://127.0.0.1:8000/createAccountError/"'))

    def testCreateAccountPostError8(self):
        ret = self.c.post('/createAccount/',
                          {'username': 'jim', 'password': 'wild', 'permission': '[1]', 'email': 'jim@this.com',
                           'firstName': 'jim', 'lastName': 'halpert', 'contactPhone': '',
                           'officePhone': '111-111-1111', 'extension': '111'}, follow=True)

        self.assertEqual(ret.status_code, 302)
        self.assertTrue(ret.content.__contains__(b'href="http://127.0.0.1:8000/createAccountError/"'))

    def testCreateAccountPostError9(self):
        ret = self.c.post('/createAccount/',
                          {'username': 'jim', 'password': 'wild', 'permission': '[1]', 'email': 'jim@this.com',
                           'firstName': 'jim', 'lastName': 'halpert', 'contactPhone': '111-111-1111',
                           'officePhone': '', 'extension': '111'}, follow=True)

        self.assertEqual(ret.status_code, 302)
        self.assertTrue(ret.content.__contains__(b'href="http://127.0.0.1:8000/createAccountError/"'))

    def testCreateAccountPostError10(self):
        ret = self.c.post('/createAccount/',
                          {'username': 'jim', 'password': 'wild', 'permission': '[1]', 'email': 'jim@this.com',
                           'firstName': 'jim', 'lastName': 'halpert', 'contactPhone': '111-111-1111',
                           'officePhone': '111-111-1111', 'extension': ''}, follow=True)

        self.assertEqual(ret.status_code, 302)
        self.assertTrue(ret.content.__contains__(b'href="http://127.0.0.1:8000/createAccountError/"'))

    def testTypes1(self):
        ret = self.c.get('/createAccount/')
        self.assertTrue(ret.content.__contains__(b'type="submit"'))

    def testTypes2(self):
        ret = self.c.get('/createAccount/')
        self.assertTrue(ret.content.__contains__(b'type="tel"'))

    def testTypes3(self):
        ret = self.c.get('/createAccount/')
        self.assertTrue(ret.content.__contains__(b'type="email"'))


    def testTypes5(self):
        ret = self.c.get('/createAccount/')
        self.assertTrue(ret.content.__contains__(b'type="number"'))
