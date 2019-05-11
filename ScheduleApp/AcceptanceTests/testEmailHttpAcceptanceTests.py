from myApp.models import USER
from django.test import TestCase
from django.test import Client

class TestEmail(TestCase):

    def setup(self):
        user = USER.objects.create(permission=[1], username="john", password="test", email="john@this.com",
                                   firstName="John", lastName="Flupper", contactPhone="2625551478",
                                   officePhone="2625487541", extension="452")

        self.c = Client()
        self.session = self.c.session
        self.session['userid'] = user.id

    def testEmailGet(self):
        response = self.client.get('/email/')
        self.assertTrue(response.content.__contains__(b'<title>Send an Email</title>'))

    def testEmailPost(self):
        c = Client()
        response = c.post('/email/', {'recipient': 'DP@this.com', 'subject': 'How much I enjoy pickels',
                                      'message': 'A whole ton homie'})

        self.assertTrue(response.status_code, 201)
        self.assertTrue(response.content.__contains__(b'<title>Email Sent</title>'))
        self.assertTrue(response.content.__contains__(b'href="http://127.0.0.1:8000/email/"'))

    def testEmailPost2(self):
        c = Client()
        response = c.post('/email/', {'recipient': 'DP@this.com', 'subject': '',
                                      'message': 'A whole ton homie'})

        self.assertTrue(response.status_code, 201)
        self.assertTrue(response.content.__contains__(b'<title>Email Sent</title>'))
        self.assertTrue(response.content.__contains__(b'href="http://127.0.0.1:8000/email/"'))

    def testEmailPostError1(self):
        c = Client()
        response = c.post('/email/', {'recipient': '', 'subject': 'How much I enjoy pickels',
                                      'message': 'A whole ton homie'})

        self.assertTrue(response.status_code, 404)
        self.assertTrue(response.content.__contains__(b'<title>Invalid recipient</title>'))
        self.assertTrue(response.content.__contains__(b'href="http://127.0.0.1:8000/email/"'))


    def testEmailPostError2(self):
       c = Client()
       response = c.post('/email/', {'recipient': 'DP@this.com', 'subject': 'How much I enjoy pickels',
                                     'message': ''})

       self.assertTrue(response.status_code, 404)
       self.assertTrue(response.content.__contains__(b'<title>Empty message</title>'))
       self.assertTrue(response.content.__contains__(b'href="http://127.0.0.1:8000/email/"'))
