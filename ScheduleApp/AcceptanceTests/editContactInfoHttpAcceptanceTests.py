from django.test import Client, TestCase
from myApp.models import USER

class AcceptanceTests(TestCase):
    def setUp(self):
        self.user = USER.objects.create(permission=[1], username="john", password="test", email="john@this.com",
                                   firstName="john", lastName="flupper", contactPhone="2628889765",
                                   officePhone="2624235436", extension="151")

        self.userToEdit = USER.objects.create(permission=[2], username="will", password="smith", email="john@this.com",
                                        firstName="john", lastName="flupper", contactPhone="2628889765",
                                        officePhone="2624235436", extension="151")
        self.user.save()
        self.userToEdit.save()

        self.c = Client()
        session = self.c.session
        session['userid'] = self.user.id
        session.save()
    def testFormMethodAction(self):
        ret = self.c.get('/editContactInfo/')
        self.assertTrue(ret.content.__contains__(b'<form method="post", action="http://127.0.0.1:8000/editContactInfo/">'))

    def testFormFields7(self):
        ret = self.c.get('/editContactInfo/')
        self.assertTrue(ret.content.__contains__(b'name="contactPhone"'))

    def testFormFields8(self):
        ret = self.c.get('/editContactInfo/')
        self.assertTrue(ret.content.__contains__(b'name="officePhone"'))

    def testFormFields9(self):
        ret = self.c.get('/editContactInfo/')
        self.assertTrue(ret.content.__contains__(b'name="extension"'))

    def testFormFields4(self):
        ret = self.c.get('/editContactInfo/')
        self.assertTrue(ret.content.__contains__(b'name="email"'))
    def testlabels4(self):
        ret = self.c.get('/editContactInfo/')
        self.assertTrue(ret.content.__contains__(b'Email'))

    def testlabels7(self):
        ret = self.c.get('/editContactInfo/')
        self.assertTrue(ret.content.__contains__(b'Contact Phone'))

    def testlabels8(self):
        ret = self.c.get('/editContactInfo/')
        self.assertTrue(ret.content.__contains__(b'Office Phone'))

    def testlabels9(self):
        ret = self.c.get('/editContactInfo/')
        self.assertTrue(ret.content.__contains__(b'Extension'))
    def correctTemplateTest(self):
        with self.assertTemplateUsed("editContactInfo"):
            self.client.get("editContactInfo")
