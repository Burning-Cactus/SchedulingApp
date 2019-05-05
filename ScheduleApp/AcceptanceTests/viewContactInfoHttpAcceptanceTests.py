from django.test import Client, TestCase
from myApp.models import USER, COURSE


# Andy
class DeleteAccountHttpAcceptanceTest(TestCase):

    def setUp(self):
        self.c = Client()
        session = self.c.session
        session['userid'] = self.user.id
        session.save()

    # HTML file tests
    def test_html_table_format(self):
        ret = self.c.get('/viewContactInfo/')
        # todo ############################################################
        self.assertTrue(ret.content.__contains__(b'type="submit"'))
        self.assertTrue(ret.content.__contains__(b'value="Submit"'))
