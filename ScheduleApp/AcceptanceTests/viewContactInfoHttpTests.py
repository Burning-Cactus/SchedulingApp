from django.test import Client, TestCase
from myApp.models import USER


class ViewContactTest(TestCase):

    def setup(self):
        self.user = USER.objects.create(permission=[3], username="teach", password="test", email="luper@this.com",
                                        firstName="semor", lastName="flupper", contactPhone="2628889765",
                                        officePhone="2624235436", extension="151")

        self.user.save()
        self.c = Client()
        session = self.c.session
        session['userid'] = self.user.id
        session.save()

    def test_get_cinfo(self):
        ret = self.c.get('/contactinfo/')
        self.assertTrue(ret.content.__contains__(b'<title>Contact Information</title>'))

    def test_post_cinfo(self):
        ret = self.c.post('/contactinfo/', follow=True)
