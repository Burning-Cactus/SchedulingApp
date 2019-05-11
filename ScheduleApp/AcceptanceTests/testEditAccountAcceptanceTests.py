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

    def testEditSelectGet(self):
        ret = self.c.get('/editSelect/')
        self.assertTrue(ret.content.__contains__(b'<title>Select User to Edit</title>'))

    def testEditSelectPost(self):
        ret = self.c.post('/editSelect/', {'userid': 2}, follow=True)
        self.assertTrue(ret.content.__contains__(b'<title>Edit User Data</title>'))
        self.assertEqual(self.userToEdit.id, self.c.session['editID'])

    def testEditAccountGet(self):
        ret = self.c.get('/editAccount/')
        self.assertTrue(ret.content.__contains__(b'<title>Edit User Data</title>'))

    def testFormMethodAction(self):
        ret = self.c.get('/editAccount/')
        self.assertTrue(ret.content.__contains__(b'<form method="post", action="http://127.0.0.1:8000/editAccount/">'))

    def testFormFields1(self):
        ret = self.c.get('/editAccount/')
        self.assertTrue(ret.content.__contains__(b'name="permission"'))

    def testFormFields2(self):
        ret = self.c.get('/editAccount/')
        self.assertTrue(ret.content.__contains__(b'name="username"'))

    def testFormFields3(self):
        ret = self.c.get('/editAccount/')
        self.assertTrue(ret.content.__contains__(b'name="password"'))

    def testFormFields4(self):
        ret = self.c.get('/editAccount/')
        self.assertTrue(ret.content.__contains__(b'name="email"'))

    def testFormFields5(self):
        ret = self.c.get('/editAccount/')
        self.assertTrue(ret.content.__contains__(b'name="firstName"'))

    def testFormFields6(self):
        ret = self.c.get('/editAccount/')
        self.assertTrue(ret.content.__contains__(b'name="lastName"'))

    def testFormFields7(self):
        ret = self.c.get('/editAccount/')
        self.assertTrue(ret.content.__contains__(b'name="contactPhone"'))

    def testFormFields8(self):
        ret = self.c.get('/editAccount/')
        self.assertTrue(ret.content.__contains__(b'name="officePhone"'))

    def testFormFields9(self):
        ret = self.c.get('/editAccount/')
        self.assertTrue(ret.content.__contains__(b'name="extension"'))

    def testFormFields10(self):
        ret = self.c.get('/editSelect/')
        self.assertTrue(ret.content.__contains__(b'name="userid"'))

    def testSubmit(self):
        ret = self.c.get('/editAccount/')
        self.assertTrue(ret.content.__contains__(b'type="submit"'))
        self.assertTrue(ret.content.__contains__(b'value=Create'))

    def testEditAccountPost1(self):
        ret = self.c.post('/editAccount/', {'UserName': 'Boso', 'Password': '', 'Permission': '', 'Email': '',
                                         'FirstName': '', 'LastName': '', 'ContactPhone': '',
                                         'OfficePhone': '', 'Extension': ''})

        self.assertTrue(ret.content.__contains__(b'<title>Commands</title>'))
        self.assertEqual(self.userToEdit.username, 'Boso')

    def testCleanSession1(self):
        self.assertEqual(self.c.session['editID'], None)

    def testEditAccountPost2(self):
        ret = self.c.post('/editAccount/', {'UserName': '', 'Password': 'foo', 'Permission': '', 'Email': '',
                                            'FirstName': '', 'LastName': '', 'ContactPhone': '',
                                            'OfficePhone': '', 'Extension': ''})

        self.assertTrue(ret.content.__contains__(b'<title>Commands</title>'))
        self.assertEqual(self.userToEdit.username, 'foo')

    def testCleanSession2(self):
        self.assertEqual(self.c.session['editID'], None)

    def testEditAccountPost3(self):
        ret = self.c.post('/editAccount/', {'UserName': '', 'Password': '', 'Permission': '[1]', 'Email': '',
                                            'FirstName': '', 'LastName': '', 'ContactPhone': '',
                                            'OfficePhone': '', 'Extension': ''})

        self.assertTrue(ret.content.__contains__(b'<title>Commands</title>'))
        self.assertEqual(self.userToEdit.username, '[1]')

    def testCleanSession3(self):
        self.assertEqual(self.c.session['editID'], None)

    def testEditAccountPost4(self):
        ret = self.c.post('/editAccount/', {'UserName': '', 'Password': '', 'Permission': '', 'Email': 'jim@jo.com',
                                            'FirstName': '', 'LastName': '', 'ContactPhone': '',
                                            'OfficePhone': '', 'Extension': ''})

        self.assertTrue(ret.content.__contains__(b'<title>Commands</title>'))
        self.assertEqual(self.userToEdit.username, 'jim@jo.com')

    def testCleanSession4(self):
        self.assertEqual(self.c.session['editID'], None)

    def testEditAccountPost5(self):
        ret = self.c.post('/editAccount/', {'UserName': '', 'Password': '', 'Permission': '', 'Email': '',
                                            'FirstName': 'lary', 'LastName': '', 'ContactPhone': '',
                                            'OfficePhone': '', 'Extension': ''})

        self.assertTrue(ret.content.__contains__(b'<title>Commands</title>'))
        self.assertEqual(self.userToEdit.username, 'lary')

    def testCleanSession5(self):
        self.assertEqual(self.c.session['editID'], None)

    def testEditAccountPost6(self):
        ret = self.c.post('/editAccount/', {'UserName': '', 'Password': '', 'Permission': '', 'Email': '',
                                            'FirstName': '', 'LastName': 'weee', 'ContactPhone': '',
                                            'OfficePhone': '', 'Extension': ''})

        self.assertTrue(ret.content.__contains__(b'<title>Commands</title>'))
        self.assertEqual(self.userToEdit.username, 'weee')

    def testCleanSession6(self):
        self.assertEqual(self.c.session['editID'], None)

    def testEditAccountPost7(self):
        ret = self.c.post('/editAccount/', {'UserName': '', 'Password': '', 'Permission': '', 'Email': '',
                                            'FirstName': '', 'LastName': '', 'ContactPhone': '121-555-5555',
                                            'OfficePhone': '', 'Extension': ''})

        self.assertTrue(ret.content.__contains__(b'<title>Commands</title>'))
        self.assertEqual(self.userToEdit.username, '121-555-5555')

    def testCleanSession7(self):
        self.assertEqual(self.c.session['editID'], None)

    def testEditAccountPost8(self):
        ret = self.c.post('/editAccount/', {'UserName': '', 'Password': '', 'Permission': '', 'Email': '',
                                            'FirstName': '', 'LastName': '', 'ContactPhone': '',
                                            'OfficePhone': '555-787-5555', 'Extension': ''})

        self.assertTrue(ret.content.__contains__(b'<title>Commands</title>'))
        self.assertEqual(self.userToEdit.username, '555-787-5555')

    def testCleanSession8(self):
        self.assertEqual(self.c.session['editID'], None)

    def testEditAccountPost9(self):
        ret = self.c.post('/editAccount/', {'UserName': '', 'Password': '', 'Permission': '', 'Email': '',
                                            'FirstName': '', 'LastName': '', 'ContactPhone': '',
                                            'OfficePhone': '', 'Extension': '1234'})

        self.assertTrue(ret.content.__contains__(b'<title>Commands</title>'))
        self.assertEqual(self.userToEdit.username, '1234')

    def testCleanSession9(self):
        self.assertEqual(self.c.session['editID'], None)

    def testlabels1(self):
        ret = self.c.get('/editAccount/')
        self.assertTrue(ret.content.__contains__(b'Username'))

    def testlabels2(self):
        ret = self.c.get('/editAccount/')
        self.assertTrue(ret.content.__contains__(b'Password'))

    def testlabels3(self):
        ret = self.c.get('/editAccount/')
        self.assertTrue(ret.content.__contains__(b'Permission'))

    def testlabels4(self):
        ret = self.c.get('/editAccount/')
        self.assertTrue(ret.content.__contains__(b'Email'))

    def testlabels5(self):
        ret = self.c.get('/editAccount/')
        self.assertTrue(ret.content.__contains__(b'First Name'))

    def testlabels6(self):
        ret = self.c.get('/editAccount/')
        self.assertTrue(ret.content.__contains__(b'Last Name'))

    def testlabels7(self):
        ret = self.c.get('/editAccount/')
        self.assertTrue(ret.content.__contains__(b'Contact Phone'))

    def testlabels8(self):
        ret = self.c.get('/editAccount/')
        self.assertTrue(ret.content.__contains__(b'Office Phone'))

    def testlabels9(self):
        ret = self.c.get('/editAccount/')
        self.assertTrue(ret.content.__contains__(b'Extension'))





