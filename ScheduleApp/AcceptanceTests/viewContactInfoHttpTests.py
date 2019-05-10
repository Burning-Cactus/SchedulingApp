from django.test import Client, TestCase
from myApp.models import USER


class ViewContactTest(TestCase):

    def setUp(self):
        self.user = USER.objects.create(permission=[1], username="semor", password="test", email="luper@this.com",
                                        firstName="semor", lastName="flupper", contactPhone="2628889765",
                                        officePhone="2624235436", extension="151")

        self.user.save()
        self.c = Client()
        session = self.c.session
        session['userid'] = self.user.id
        session.save()

    def testViewContactInfoGet1(self):
        with self.assertTemplateUsed('shell/viewContactInfo.html'):
            ret = self.c.get('/viewContactInfo/')
        self.assertTrue(ret.content.__contains__(b'<title>Public Contact Info</title>'))

    def testViewContactInfoGet2(self):
        ret = self.c.get('/viewContactInfo/')
        self.assertTrue(ret.content.__contains__(b'Contact Info'))

    def test_viewContactInfo_if_using_table(self):
        ret = self.c.get('/viewContactInfo/')
        self.assertTrue(ret.content.__contains__(b'<table'))
