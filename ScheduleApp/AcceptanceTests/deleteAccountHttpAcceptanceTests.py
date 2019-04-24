from django.test import Client, TestCase
from myApp.models import USER
from django.urls import reverse


class DeleteAccountHttpAcceptanceTest(TestCase):

    def setUp(self):
        self.user = USER.objects.create(permission=[4], username="john", password="test", email="john@this.com",
                                        firstName="john", lastName="flupper", contactPhone="2628889765",
                                        officePhone="2624235436", extension="151")

    # Tests a properly used delete page
        # returns a status_code equal to 200
    def test1(self):
        c = Client()
        response = c.post('/delete/', {'username': 'john', 'password': 'smith', 'databaseID': '-1337'})
        #response = c.get('/customer/details/')
        TestCase.assertEqual(response.status_code, 200)

        # check databaseID
        # looking at session and make sure it is equal to something?



