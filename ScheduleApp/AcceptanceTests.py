from django.test import TestCase
from ScheduleApp import Commands, User, Course
from myApp.models import LAB_SECTION, COURSE, A_LIST, USER, I_LIST
from myApp.models import Terminal


class AcceptanceTests(TestCase):
    def setUp(self):
        LAB_SECTION.objects.create(databaseID=1, name="Physics", courseNumber=500, classNumber=270, time="9-10am",
                                   location="Physics 270")

        USER.objects.create(permission=[2], username="IPO", password="pret212", databaseID=69, email="IPO@DEZN.com",
                            firstName="Bo", lastName="fa", contactPhone="2625874132", officePhone="2625478669",
                            extension="148")

        COURSE.objects.create(databaseID=645, name="DEATHSCI", courseNumber=500, classNumber=204,
                              labList=[804, 803, 802], time="8-9am", location="EMS 203")

        A_LIST.objects.create(courseID=68, assistantID=67)
        I_LIST.objects.create(courseID=56, instructorID=75)

    def test_login(self):
        userdata = USER.objects.get(databaseID=69)
        user = User.User(userdata.permission, userdata.username, userdata.password,
                         userdata.databaseID, userdata.email, userdata.firstName,
                         userdata.lastName, userdata.contactPhone, userdata.officePhone, userdata.extension)
        self.assertEquals(Terminal.login(user.username, user.password), "Login Successful")
        self.assertEquals(Terminal.login(user.username, 'wrong'), "Invalid Login")
        self.assertEquals(Terminal.login('IPPPO', user.password), "Invalid Login")
        self.assertEquals(Terminal.login('IPPPPOOOOO', 'wronggggggg'), "Invalid Login")

    def test_logout(self):
        self.assertEquals(Terminal.logout(), "No User Logged In")
        userdata = USER.objects.get(databaseID=69)
        user = User.User(userdata.permission, userdata.username, userdata.password,
                         userdata.databaseID, userdata.email, userdata.firstName,
                         userdata.lastName, userdata.contactPhone, userdata.officePhone, userdata.extension)
        Terminal.login(user.username, user.password)
        self.assertEquals(Terminal.logout(), "Successfully Logged Out")
        self.assertEquals(Terminal.logout(), "No User Logged In")

    def test_createAccount(self):
        self.assertEquals(Terminal.createAccount('3', 'jjj', 'aaa', 'jjj@gmail.com', 'John', 'Aponte', '2011111111',
                                                 '2012222222', '47'), "Account Successfully Created")

        self.assertEqual(Terminal.createAccount('3', 'jjj', 'aaa', 'jjj@gmail.com', 'John', 'Aponte', '2011111111',
                                                '2012222222', '47'), "Account Already Exists")

        self.assertEqual(Terminal.createAccount('4', 'bbb', 'ccc', 'bbb@gmail.com', 'John', 'Aponte', '2033333333',
                                                '2044444444', '48'), "Account Successfully Created")

        self.assertEqual(Terminal.createAccount('2', 'bbb', 'ccc', 'ddd@gmail.com', 'Hn', 'Te', '2055555555',
                                                '2066666666', '49'), "Username Already Exist")

        self.assertEqual(Terminal.createAccount('1', 'eee', 'zzz', 'ddd@gmail.com', 'Jo', 'Ap', '2066666666',
                                                '207777777', '48'), "Email Already In Use")

        self.assertEqual(Terminal.createAccount('3', 'hhh', 'yyy', 'uuu@gmail.com', 'Doom', 'Kek', '2066666666',
                                                '2044444444', '48'), "Phone Number Already in Use")

        self.assertEqual(Terminal.createAccount('0', 'hhh', 'yyy', 'uuu@gmail.com', 'Doom', 'Kek', '2066666666',
                                                '2044444444', '48'), "Invalid Permission")

        self.assertEqual(Terminal.createAccount('5', 'hhh', 'yyy', 'uuu@gmail.com', 'Doom', 'Kek', '2066666666',
                                                '2044444444', '48'), "Invalid Permission")

        self.assertEqual(Terminal.createAccount('3', '', 'yyy', 'uuu@gmail.com', 'Doom', 'Kek', '2066666666',
                                                '2044444444', '48'), "Invalid Username")

        self.assertEqual(Terminal.createAccount('3', 'hhh', '', 'uuu@gmail.com', 'Doom', 'Kek', '2066666666',
                                                '2044444444', '48'), "Invalid Password")

        self.assertEqual(Terminal.createAccount('3', 'hhh', 'yyy', 'dfsiahfilnwefr', 'Doom', 'Kek', '2066666666',
                                                '2044444444', '48'), "Invalid Email")

        self.assertEqual(Terminal.createAccount('3', 'hhh', 'yyy', '', 'Doom', 'Kek', '2066666666',
                                                '2044444444', '48'), "Invalid Email")

        self.assertEqual(Terminal.createAccount('3', 'hhh', 'yyy', 'uuu@gmail.com', '', 'Kek', '2066666666',
                                                '2044444444', '48'), "Must Enter Valid Name")

        self.assertEqual(Terminal.createAccount('3', 'hhh', 'yyy', 'uuu@gmail.com', 'Doom', '', '2066666666',
                                                '2044444444', '48'), "Must Enter Valid Name")

        self.assertEqual(
            Terminal.createAccount('3', 'hhh', 'yyy', 'uuu@gmail.com', 'Doom', 'Kek', '4535387478347874878247',
                                   '2044444444', '48'), "Invalid Phone Number")

        self.assertEqual(Terminal.createAccount('3', 'hhh', 'yyy', 'uuu@gmail.com', 'Doom', 'Kek', '12334',
                                                '2044444444', '48'), "Invalid Phone Number")

        self.assertEqual(Terminal.createAccount('3', ' ', 'yyy', 'uuuw@wgmawefwefwefwefil.cowefwefm', 'Do2om', '11',
                                                '2063242342346666666',
                                                '204444444423244', '4238'), "Multiple Invalid Credentials")

    def test_editAccount(self):
        userdata = USER.objects.get(databaseID=69)
        user = User.User(userdata.permission, userdata.username, userdata.password,
                         userdata.databaseID, userdata.email, userdata.firstName,
                         userdata.lastName, userdata.contactPhone, userdata.officePhone, userdata.extension)
        self.assertEqual(Terminal.editAccount(user.databaseID), "What Would You Like To Edit?")
        self.assertEqual(Terminal.editAccount('231231'), "User Not Found")

    def test_deleteAccount(self):
        userdata = USER.objects.get(databaseID=69)
        user = User.User(userdata.permission, userdata.username, userdata.password,
                         userdata.databaseID, userdata.email, userdata.firstName,
                         userdata.lastName, userdata.contactPhone, userdata.officePhone, userdata.extension)
        self.assertEqual(Terminal.deleteAccount('314351'), "User Not Found")
        self.assertEqual(Terminal.deleteAccount(user.databaseID), "Account Deleted")

    ## courseData = COURSE.objects.get(databaseID=645)
    ##course = COURSE.Course(courseData.databaseID, courseData.name, courseData.courseNumber, courseData.classNumber,
##         courseData.labList, courseData.time, courseData.location)