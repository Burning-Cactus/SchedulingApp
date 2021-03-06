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
        self.assertTrue(ret.content.__contains__(b'<form method="post", action="http://127.0.0.1:8000/createAccount/">'))

    def testFormFields1(self):
        ret = self.c.get('/createAccount/')
        self.assertTrue(ret.content.__contains__(b'name="permission"'))

    def testFormFields2(self):
        ret = self.c.get('/createAccount/')
        self.assertTrue(ret.content.__contains__(b'name="username"'))

    def testFormFields3(self):
        ret = self.c.get('/createAccount/')
        self.assertTrue(ret.content.__contains__(b'name="password"'))

    def testFormFields4(self):
        ret = self.c.get('/createAccount/')
        self.assertTrue(ret.content.__contains__(b'name="email"'))

    def testFormFields5(self):
        ret = self.c.get('/createAccount/')
        self.assertTrue(ret.content.__contains__(b'name="firstName"'))

    def testFormFields6(self):
        ret = self.c.get('/createAccount/')
        self.assertTrue(ret.content.__contains__(b'name="lastName"'))

    def testFormFields7(self):
        ret = self.c.get('/createAccount/')
        self.assertTrue(ret.content.__contains__(b'name="contactPhone"'))

    def testFormFields8(self):
        ret = self.c.get('/createAccount/')
        self.assertTrue(ret.content.__contains__(b'name="officePhone"'))

    def testFormFields9(self):
        ret = self.c.get('/createAccount/')
        self.assertTrue(ret.content.__contains__(b'name="extension"'))

    def testSubmit(self):
        ret = self.c.get('/createAccount/')
        self.assertTrue(ret.content.__contains__(b'type="submit"'))
        self.assertTrue(ret.content.__contains__(b'value="Create"'))

    def testCreateAccountPost(self):
        ret = self.c.post('/createAccount/', {'userName': 'jim', 'password': 'wild', 'permission': '[1]', 'email': 'jim@this.com',
                                               'firstName': 'jim', 'lastName': 'halpert', 'contactPhone': '111-111-1111',
                                               'officePhone': '111-111-1111', 'extension': '111'})

        self.assertEqual(ret.status_code, 302)
        self.assertTrue(ret.conent.__contains__(b'<title>Account Created</title>'))
        self.assertTrue(ret.conent.__contains__(b'href="http://127.0.0.1:8000/home/"'))

    def testCreateAccountPostError1(self):
        ret = self.c.post('/createAccount/',
                          {'userName': '', 'password': 'wild', 'permission': '[1]', 'email': 'jim@this.com',
                           'firstName': 'jim', 'lastName': 'halpert', 'contactPhone': '111-111-1111',
                           'officePhone': '111-111-1111', 'extension': '111'})

        self.assertTrue(ret.conent.__contains__(b'<title>Create Account Error</title>'))
        self.assertTrue(ret.conent.__contains__(b'href="http://127.0.0.1:8000/createAccount/"'))

    def testCreateAccountPostError2(self):
        ret = self.c.post('/createAccount/',
                          {'userName': 'jim', 'password': 'wild', 'permission': '[1]', 'email': 'jim@this.com',
                           'firstName': 'jim', 'lastName': 'halpert', 'contactPhone': '111-111-1111',
                           'officePhone': '111-111-1111', 'extension': '111'})

        self.assertTrue(ret.conent.__contains__(b'<title>Create Account Error</title>'))
        self.assertTrue(ret.conent.__contains__(b'href="http://127.0.0.1:8000/createAccount/"'))

    def testCreateAccountPostError3(self):
        ret = self.c.post('/createAccount/',
                          {'userName': 'jim', 'password': '', 'permission': '[1]', 'email': 'jim@this.com',
                           'firstName': 'jim', 'lastName': 'halpert', 'contactPhone': '111-111-1111',
                           'officePhone': '111-111-1111', 'extension': '111'})

        self.assertTrue(ret.conent.__contains__(b'<title>Create Account Error</title>'))
        self.assertTrue(ret.conent.__contains__(b'href="http://127.0.0.1:8000/createAccount/"'))

    def testCreateAccountPostError4(self):
        ret = self.c.post('/createAccount/',
                          {'userName': 'jim', 'password': 'wild', 'permission': '', 'email': 'jim@this.com',
                           'firstName': 'jim', 'lastName': 'halpert', 'contactPhone': '111-111-1111',
                           'officePhone': '111-111-1111', 'extension': '111'})

        self.assertTrue(ret.conent.__contains__(b'<title>Create Account Error</title>'))
        self.assertTrue(ret.conent.__contains__(b'href="http://127.0.0.1:8000/createAccount/"'))

    def testCreateAccountPostError5(self):
        ret = self.c.post('/createAccount/',
                          {'userName': 'jim', 'password': 'wild', 'permission': '[1]', 'email': '',
                           'firstName': 'jim', 'lastName': 'halpert', 'contactPhone': '111-111-1111',
                           'officePhone': '111-111-1111', 'extension': '111'})

        self.assertTrue(ret.conent.__contains__(b'<title>Create Account Error</title>'))
        self.assertTrue(ret.conent.__contains__(b'href="http://127.0.0.1:8000/createAccount/"'))

    def testCreateAccountPostError6(self):
        ret = self.c.post('/createAccount/',
                          {'userName': 'jim', 'password': 'wild', 'permission': '[1]', 'email': 'jim@this.com',
                           'firstName': '', 'lastName': 'halpert', 'contactPhone': '111-111-1111',
                           'officePhone': '111-111-1111', 'extension': '111'})

        self.assertTrue(ret.conent.__contains__(b'<title>Create Account Error</title>'))
        self.assertTrue(ret.conent.__contains__(b'href="http://127.0.0.1:8000/createAccount/"'))

    def testCreateAccountPostError7(self):
        ret = self.c.post('/createAccount/',
                          {'userName': 'jim', 'password': 'wild', 'permission': '[1]', 'email': 'jim@this.com',
                           'firstName': 'jim', 'lastName': '', 'contactPhone': '111-111-1111',
                           'officePhone': '111-111-1111', 'extension': '111'})

        self.assertTrue(ret.conent.__contains__(b'<title>Create Account Error</title>'))
        self.assertTrue(ret.conent.__contains__(b'href="http://127.0.0.1:8000/createAccount/"'))

    def testCreateAccountPostError8(self):
        ret = self.c.post('/createAccount/',
                          {'userName': 'jim', 'password': 'wild', 'permission': '[1]', 'email': 'jim@this.com',
                           'firstName': 'jim', 'lastName': 'halpert', 'contactPhone': '',
                           'officePhone': '111-111-1111', 'extension': '111'})

        self.assertTrue(ret.conent.__contains__(b'<title>Create Account Error</title>'))
        self.assertTrue(ret.conent.__contains__(b'href="http://127.0.0.1:8000/createAccount/"'))

    def testCreateAccountPostError9(self):
        ret = self.c.post('/createAccount/',
                          {'userName': 'jim', 'password': 'wild', 'permission': '[1]', 'email': 'jim@this.com',
                           'firstName': 'jim', 'lastName': 'halpert', 'contactPhone': '111-111-1111',
                           'officePhone': '', 'extension': '111'})

        self.assertTrue(ret.conent.__contains__(b'<title>Create Account Error</title>'))
        self.assertTrue(ret.conent.__contains__(b'href="http://127.0.0.1:8000/createAccount/"'))

    def testCreateAccountPostError10(self):
        ret = self.c.post('/createAccount/',
                          {'userName': 'jim', 'password': 'wild', 'permission': '[1]', 'email': 'jim@this.com',
                           'firstName': 'jim', 'lastName': 'halpert', 'contactPhone': '111-111-1111',
                           'officePhone': '111-111-1111', 'extension': ''})

        self.assertTrue(ret.conent.__contains__(b'<title>Create Account Error</title>'))
        self.assertTrue(ret.conent.__contains__(b'href="http://127.0.0.1:8000/createAccount/"'))

    def testTypes1(self):
        ret = self.c.get('/createAccount/')
        self.assertTrue(ret.content.__contains__(b'type="submit"'))

    def testTypes2(self):
        ret = self.c.get('/createAccount/')
        self.assertTrue(ret.content.__contains__(b'type="tel"'))

    def testTypes3(self):
        ret = self.c.get('/createAccount/')
        self.assertTrue(ret.content.__contains__(b'type="email"'))

    def testTypes4(self):
        ret = self.c.get('/createAccount/')
        self.assertTrue(ret.content.__contains__(b'type="name"'))

    def testTypes5(self):
        ret = self.c.get('/createAccount/')
        self.assertTrue(ret.content.__contains__(b'type="number"'))






