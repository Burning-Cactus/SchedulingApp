from django.test import Client, TestCase
from ScheduleApp import User
from myApp.models import USER

class AcceptanceTests(TestCase):
    def setUp(self):
        self.user = USER.objects.create(permission=[4], username="john", password="test", email="john@this.com",
                                        firstName="john", lastName="flupper", contactPhone="2628889765",
                                        officePhone="2624235436", extension="151")



    def editAccountTests(self):
        c = Client()
        go = c.post('editAccount.html', {'UserName': '~', 'Password': '~', 'Permission': '~', 'Email': '~', 'FirstName':
                                         '~', 'LastName': '~', 'ContactPhone': '000-000-0000', 'OfficePhone':
                                         '000-000-0000', 'Extension': '~'})
        url = go.redirect_chain
        self.assertEquals(url, ['http://127.0.0.1:8000/home'])

        self.assertEqual(USER.objects.get(id=self.user.id), )

