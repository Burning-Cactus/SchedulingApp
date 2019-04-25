from django.test import Client
from django.test import TestCase
from myApp.models import USER


class CreateAccountTest(TestCase):

    def setup(self):
        self.user = USER.objects.create(permission=[1], username="john", password="test", email="john@this.com",
                                        firstName="john", lastName="flupper", contactPhone="2628889765",
                                        officePhone="2624235436", extension="151")

    # Test to make sure the url is set correctly
    def testUrl(self):
        c = Client()
        response = c.get('/createAccount/')
        url = response.status_code
        self.assertEquals(url, 200)

    # Test the functionality of creating an Account
    def testFunc(self):
        c = Client()
        info = ['3', 'jjj', 'aaa', 'jjj@gmail.com', 'John', 'Aponte', '2011111111', '2012222222', '47']
        response = c.get('/createAccount/', data=info)
        self.assertEquals(response.context['permission'], '3')
