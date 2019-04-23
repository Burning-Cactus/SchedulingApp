from django.test import Client
from ScheduleApp import User

class AcceptanceTests(Client):
    def editAccountTests(self):
        c = Client()
        c.post('editAccount.html', {'UserName': 'Boi', 'Password': '~', 'Permission': '~', 'Email': '~', 'FirstName':
                                    '~','LastName':'~', 'ContactPhone': '000-000-0000', 'OfficePhone': '000-000-0000',
                                    'Extension': '~'})
        
