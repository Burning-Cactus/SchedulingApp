from django.test import Client
from django.test import TestCase
from myApp.models import USER


class AccessDataTestsNegative(TestCase):

    def setUp(self):
        self.user = USER.objects.create(permission=[3], username="semor", password="test", email="luper@this.com",
                                        firstName="semor", lastName="flupper", contactPhone="2628889765",
                                        officePhone="2624235436", extension="151")

        self.user.save()
        self.c = Client()
        session = self.c.session
        session['userid'] = self.user.id
        session.save()




    def testAccessDataGet1(self):
        ret = self.c.get('/accessAllData/')
        self.assertTrue(ret.content.__contains__(b'<title>Permission Denied</title>'))
        self.assertTrue(ret.content.__contains__(b'href="http://127.0.0.1:8000/createAccount/"'))


