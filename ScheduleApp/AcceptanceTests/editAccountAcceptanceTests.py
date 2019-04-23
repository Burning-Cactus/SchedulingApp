from django.test import Client, TestCase
from ScheduleApp import User

class AcceptanceTests(TestCase):
    def editAccountTests(self):
        c = Client()
        newUser = User
        c.post('editAccount.html', {'UserName': 'Boi', 'Password': '~', 'Permission': '~', 'Email': '~', 'FirstName':
                                    '~', 'LastName': '~', 'ContactPhone': '000-000-0000', 'OfficePhone': '000-000-0000',
                                    'Extension': '~'})


