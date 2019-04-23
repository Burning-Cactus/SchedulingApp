from django.test import Client

class AcceptanceTests(Client):
    def editAccountTests(self):
        c = Client()
        c.post('editAccount.html', {'UserName': 'Boi', 'Password': '~'})