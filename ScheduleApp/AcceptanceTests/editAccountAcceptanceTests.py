from django.test import Client, TestCase
from myApp.models import USER

class AcceptanceTests(TestCase):

    def editSelectTests(self):
        pass

    def editAccountTests(self):
        memes = USER.objects.create(permission=[4], username="john", password="test", email="john@this.com",
                                    firstName="john", lastName="flupper", contactPhone="2628889765",
                                    officePhone="2624235436", extension="151")
        c = Client()
        #idToEdit = memes.id
        #ro = c.post('editSelect.html', {'UserId': idToEdit})
        #url = ro.redirect_chain
        #self.assertEquals(url, ['editAccount.html'])

        go = c.post('editAccount.html', {'UserName': 'Boso', 'Password': '~', 'Permission': '~', 'Email': '~',
                                         'FirstName': '~', 'LastName': '~', 'ContactPhone': '~',
                                         'OfficePhone': '~', 'Extension': '~'})
        #url = go.redirect_chain
        #self.assertEquals(url, ['http://127.0.0.1:8000/home'])

        self.assertEqual(USER.objects.get(c.session['editID']).username, 'Boso')

        #self.assertEqual(c.session['editID'].username, 'Mozo')

