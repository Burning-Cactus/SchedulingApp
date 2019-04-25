from django.test import Client, TestCase
<<<<<<< HEAD
<<<<<<< HEAD
from myApp.models import USER
=======
from django.urls import reverse
from . import views
>>>>>>> parent of 215c56f... Added the setUp method
=======
from django.urls import reverse
from . import views
>>>>>>> parent of 215c56f... Added the setUp method


# Andy
class DeleteAccountHttpAcceptanceTest(TestCase):

<<<<<<< HEAD
<<<<<<< HEAD
    def setUp(self):
        memes = USER.objects.create(permission=[4], username="john", password="test", email="john@this.com",
                                    firstName="john", lastName="flupper", contactPhone="2628889765",
                                    officePhone="2624235436", extension="151")

=======
>>>>>>> parent of 215c56f... Added the setUp method
=======
>>>>>>> parent of 215c56f... Added the setUp method
    # Tests a properly used delete page
        # returns a status_code equal to 200
    def deleteAccountTest(self):
        self.setUp()
        c = Client()
        idToDelete = c.session[USER.objects.get(username="john")]

        # Go to the delete user selection page
        ro = c.post('deleteSelect.html', {'UserId': idToDelete})

        # Make sure we redirect to the proper page for deleting
        url = ro.redirect_chain
        self.assertEquals(url, ['deleteAccount.html'])

        # delete UserId
        go = c.post('deleteAccount.html')

        # after deleted, go home
        url = go.redirect_chain
        self.assertEquals(url, ['http://127.0.0.1:8000/home'])

        # Check to ensure that the user is gone
        self.assertEqual(c.session['UserId'], None)
