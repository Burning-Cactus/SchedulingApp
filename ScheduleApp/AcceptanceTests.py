from django.test import TestCase
from ScheduleApp import Commands, User, Course
from myApp.models import LAB_SECTION, COURSE, A_LIST, USER, I_LIST
from myApp.models import Terminal



class AcceptanceTests(TestCase):
    def setUp(self):
        LAB_SECTION.objects.create(databaseID=1, name="Physics", courseNumber=500, classNumber=270, time="9-10am",
                                   location="Physics 270")

        USER.objects.create(permission=[1], username="IPO", password="pret212", databaseID=69, email="IPO@DEZN.com",
                            firstName="Bo", lastName="fa", contactPhone="2625874132", officePhone="2625478669",
                            extension="148")
        USER.objects.create(permission=[2], username="Dio", password="pret123", databaseID=70, email="Dio@gmail.com",
                            firstName="Dezn", lastName="Uts", contactPhone="2621111223", officePhone="262753865",
                            extension="149")
        USER.objects.create(permission=[3], username="Jotaro", password="pret12", databaseID=71, email="Jotaro@yahoo.com",
                            firstName="Lig", lastName="Ma", contactPhone="2628377456", officePhone="2629846210",
                            extension="150")
        USER.objects.create(permission=[4], username="Poyo", password="pret2", databaseID=72, email="Poyo@hotmail.com",
                            firstName="Bo", lastName="fa", contactPhone="2628889765", officePhone="2624235436",
                            extension="151")

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
        userdata = USER.objects.get(databaseID=69)
        user = User.User(userdata.permission, userdata.username, userdata.password,
                         userdata.databaseID, userdata.email, userdata.firstName,
                         userdata.lastName, userdata.contactPhone, userdata.officePhone, userdata.extension)
        userdata2 = USER.objects.get(databaseID=70)
        user2 = User.User(userdata2.permission, userdata2.username, userdata2.password,
                          userdata2.databaseID, userdata2.email, userdata2.firstName,
                          userdata2.lastName, userdata2.contactPhone, userdata2.officePhone, userdata2.extension)
        userdata3 = USER.objects.get(databaseID=71)
        user3 = User.User(userdata3.permission, userdata3.username, userdata3.password,
                          userdata3.databaseID, userdata3.email, userdata3.firstName,
                          userdata3.lastName, userdata3.contactPhone, userdata3.officePhone, userdata3.extension)

        self.assertEqual(user.permission == 1 | user.permission == 2)
        self.assertEqual(user2.permission == 1 | user2.permission == 2)
        self.assertTrue((user3.permission != 1 | user2.permission == 2), "Not Authorized To Use This Command")
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

        # Instead of having a general error, have the errors listed by the order of their fault. ex: the username in the
        # first error so it would spit out "Invalid username", then once its fixed, it would spit out "Invalid Email"
        self.assertEqual(Terminal.createAccount('3', ' ', 'yyy', 'uuuw@wgmawefwefwefwefil.cowefwefm', 'Do2om', '11',
                                                '2063242342346666666',
                                                '204444444423244', '4238'), "Multiple Invalid Credentials")

    def test_editAccount(self):
        userdata = USER.objects.get(databaseID=69)
        user = User.User(userdata.permission, userdata.username, userdata.password,
                         userdata.databaseID, userdata.email, userdata.firstName,
                         userdata.lastName, userdata.contactPhone, userdata.officePhone, userdata.extension)
        userdata2 = USER.objects.get(databaseID=70)
        user2 = User.User(userdata2.permission, userdata2.username, userdata2.password,
                          userdata2.databaseID, userdata2.email, userdata2.firstName,
                          userdata2.lastName, userdata2.contactPhone, userdata2.officePhone, userdata2.extension)
        userdata3 = USER.objects.get(databaseID=71)
        user3 = User.User(userdata3.permission, userdata3.username, userdata3.password,
                          userdata3.databaseID, userdata3.email, userdata3.firstName,
                          userdata3.lastName, userdata3.contactPhone, userdata3.officePhone, userdata3.extension)

        self.assertEqual(user.permission == 1 | user.permission == 2)
        self.assertEqual(user2.permission == 1 | user2.permission == 2)
        self.assertTrue((user3.permission != 1 & user2.permission == 2), "Not Authorized To Use This Command")

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
        userdata2 = USER.objects.get(databaseID=70)
        user2 = User.User(userdata2.permission, userdata2.username, userdata2.password,
                          userdata2.databaseID, userdata2.email, userdata2.firstName,
                          userdata2.lastName, userdata2.contactPhone, userdata2.officePhone, userdata2.extension)
        userdata3 = USER.objects.get(databaseID=71)
        user3 = User.User(userdata3.permission, userdata3.username, userdata3.password,
                          userdata3.databaseID, userdata3.email, userdata3.firstName,
                          userdata3.lastName, userdata3.contactPhone, userdata3.officePhone, userdata3.extension)

        self.assertEqual(user.permission == 1 | user.permission == 2)
        self.assertEqual(user2.permission == 1 | user2.permission == 2)
        self.assertTrue((user3.permission != 1 & user2.permission == 2), "Not Authorized To Use This Command")

        userdata = USER.objects.get(databaseID=69)
        user = User.User(userdata.permission, userdata.username, userdata.password,
                         userdata.databaseID, userdata.email, userdata.firstName,
                         userdata.lastName, userdata.contactPhone, userdata.officePhone, userdata.extension)
        self.assertEqual(Terminal.deleteAccount('314351'), "User Not Found")
        self.assertEqual(Terminal.deleteAccount(user.databaseID), "Account Deleted")


    def test_createCourse(self):
        userdata = USER.objects.get(databaseID=69)
        user = User.User(userdata.permission, userdata.username, userdata.password,
                         userdata.databaseID, userdata.email, userdata.firstName,
                         userdata.lastName, userdata.contactPhone, userdata.officePhone, userdata.extension)
        userdata2 = USER.objects.get(databaseID=70)
        user2 = User.User(userdata2.permission, userdata2.username, userdata2.password,
                          userdata2.databaseID, userdata2.email, userdata2.firstName,
                          userdata2.lastName, userdata2.contactPhone, userdata2.officePhone, userdata2.extension)
        userdata3 = USER.objects.get(databaseID=71)
        user3 = User.User(userdata3.permission, userdata3.username, userdata3.password,
                          userdata3.databaseID, userdata3.email, userdata3.firstName,
                          userdata3.lastName, userdata3.contactPhone, userdata3.officePhone, userdata3.extension)

        self.assertEqual(user.permission == 1 | user.permission == 2)
        self.assertEqual(user2.permission == 1 | user2.permission == 2)
        self.assertTrue((user3.permission != 1 & user2.permission == 2), "Not Authorized To Use This Command")

        courseData = COURSE.objects.get(databaseID=645)
        course = COURSE.Course(courseData.databaseID, courseData.name, courseData.courseNumber, courseData.classNumber,
        courseData.labList, courseData.time, courseData.location)
        self.assertEqual(Terminal.createCourse(course.name, course.courseNumber, course.classnumber, course.time,
                                                course.location), "Course Has Been Created")

        self.assertEqual(Terminal.createCourse(course.name, course.courseNumber, course.classnumber, course.time,
                                               course.location), "Course Already Exists")

        self.assertEqual(Terminal.createCourse('sdfs)gfsfw:::::', course.courseNumber, course.classnumber, course.time,
                                               course.location), "Invalid name")

        self.assertEqual(Terminal.createCourse(course.name, 'sdkjfbdf', course.classnumber, course.time,
                                               course.location), "Invalid Course Number")

        self.assertEqual(Terminal.createCourse(course.name, course.courseNumber, '34kb23id', course.time,
                                               course.location), "Invalid Class Number")

        self.assertEqual(Terminal.createCourse(course.name, course.courseNumber, course.classnumber, 'sdffw',
                                               course.location), "Invalid Time")

        self.assertEqual(Terminal.createCourse(course.name, course.courseNumber, course.classnumber, course.time,
                                               'eq2"kbt'), "Invalid Location")
        #Have in order error reports
        self.assertEqual(Terminal.createCourse('eiufb23]]u', 'sdfsdf', 'wefwvfwe','wergewrg',
                                               'wefwefwef"'), "Multiple Invalid Info")


    def test_email(self):
        userdata = USER.objects.get(databaseID=69)
        user = User.User(userdata.permission, userdata.username, userdata.password,
                         userdata.databaseID, userdata.email, userdata.firstName,
                         userdata.lastName, userdata.contactPhone, userdata.officePhone, userdata.extension)
        userdata2 = USER.objects.get(databaseID=70)
        user2 = User.User(userdata2.permission, userdata2.username, userdata2.password,
                          userdata2.databaseID, userdata2.email, userdata2.firstName,
                          userdata2.lastName, userdata2.contactPhone, userdata2.officePhone, userdata2.extension)
        userdata3 = USER.objects.get(databaseID=71)
        user3 = User.User(userdata3.permission, userdata3.username, userdata3.password,
                          userdata3.databaseID, userdata3.email, userdata3.firstName,
                          userdata3.lastName, userdata3.contactPhone, userdata3.officePhone, userdata3.extension)
        userdata4 = USER.objects.get(databaseID=72)
        user4 = User.User(userdata4.permission, userdata4.username, userdata4.password,
                          userdata4.databaseID, userdata4.email, userdata4.firstName,
                          userdata4.lastName, userdata4.contactPhone, userdata4.officePhone, userdata4.extension)

        self.assertEqual(user.permission == 1 | user.permission == 2 | user.permission == 3)
        self.assertEqual(user2.permission == 1 | user2.permission == 2 | user2.permission == 3)
        self.assertEqual(user3.permission == 1 | user3.permission == 2 | user3. permission == 3)
        self.assertTrue((user4.permission != 1 & user4.permission == 2 & user4.permission == 3), "Not Authorized To Use This Command")

        #SHould we have a user present with the wrong permissions so we can have a fail scenario?
        self.assertEqual(Terminal.email("Hello World"), "Message Sent")


    def test_accessData(self):
        userdata = USER.objects.get(databaseID=69)
        user = User.User(userdata.permission, userdata.username, userdata.password,
                         userdata.databaseID, userdata.email, userdata.firstName,
                         userdata.lastName, userdata.contactPhone, userdata.officePhone, userdata.extension)
        userdata2 = USER.objects.get(databaseID=70)
        user2 = User.User(userdata2.permission, userdata2.username, userdata2.password,
                          userdata2.databaseID, userdata2.email, userdata2.firstName,
                          userdata2.lastName, userdata2.contactPhone, userdata2.officePhone, userdata2.extension)

        userdata3 = USER.objects.get(databaseID=71)
        user3 = User.User(userdata3.permission, userdata3.username, userdata3.password,
                          userdata3.databaseID, userdata3.email, userdata3.firstName,
                          userdata3.lastName, userdata3.contactPhone, userdata3.officePhone, userdata3.extension)
        userdata4 = USER.objects.get(databaseID=72)
        user4 = User.User(userdata4.permission, userdata4.username, userdata4.password,
                          userdata4.databaseID, userdata4.email, userdata4.firstName,
                          userdata4.lastName, userdata4.contactPhone, userdata4.officePhone, userdata4.extension)
        courseData = COURSE.objects.get(databaseID=645)
        course = COURSE.Course(courseData.databaseID, courseData.name, courseData.courseNumber, courseData.classNumber,
                               courseData.labList, courseData.time, courseData.location)
        self.assertEqual(user.permission == 1 | user.permission == 2)
        self.assertEqual(user2.permission == 1 | user2.permission == 2)
        self.assertTrue(user3.permission != 1 | user3.permission != 2 )
        self.assertTrue((user4.permission != 1 & user4.permission == 2 ),
                        "Not Authorized To Use This Command")

        self.assertEqual(Terminal.accessData(), user.permission + " " + user.username + " " + user.password
                         + " " + user.databaseID + " " + user.email + " " + user.firstName + " " + user.lastName + " " + user.contactPhone
                         + " " + user.officePhone + " " + user.extension + "\n " + user2.permission + " " + user2.username + " " + user2.password
                       + " " + user2.databaseID + " " + user2.email + " " + user2.firstName + " " + user2.lastName + " " + user2.contactPhone
                         + " " + user2.officePhone + " " + user2.extension + "\n " + user3.permission + " " + user3.username + " " + user3.password
                         + " " + user3.databaseID + " " + user3.email + " " + user3.firstName + " " + user3.lastName + " " + user3.contactPhone
                 + " " + user3.officePhone + " " +user3.extension + "\n " + user4.permission + user4.username + user4.password +
                 user4.databaseID + " " + user4.email + " " + user4.firstName + " " + user4.lastName + " " + user4.contactPhone
                         + " " + user4.officePhone + " " + user4.extension + "\n " + course.databaseID + " " + course.name + " " +
                course.courseNumber + " " + course.classNumber + " " + course.labList + " " + course.time + " " +course.location)

    def test_assignInstructorToCourse(self):
        userdata = USER.objects.get(databaseID=69)
        user = User.User(userdata.permission, userdata.username, userdata.password,
                         userdata.databaseID, userdata.email, userdata.firstName,
                         userdata.lastName, userdata.contactPhone, userdata.officePhone, userdata.extension)
        userdata2 = USER.objects.get(databaseID=70)
        user2 = User.User(userdata2.permission, userdata2.username, userdata2.password,
                          userdata2.databaseID, userdata2.email, userdata2.firstName,
                          userdata2.lastName, userdata2.contactPhone, userdata2.officePhone, userdata2.extension)

        userdata3 = USER.objects.get(databaseID=71)
        user3 = User.User(userdata3.permission, userdata3.username, userdata3.password,
                          userdata3.databaseID, userdata3.email, userdata3.firstName,
                          userdata3.lastName, userdata3.contactPhone, userdata3.officePhone, userdata3.extension)
        userdata4 = USER.objects.get(databaseID=72)
        user4 = User.User(userdata4.permission, userdata4.username, userdata4.password,
                          userdata4.databaseID, userdata4.email, userdata4.firstName,
                          userdata4.lastName, userdata4.contactPhone, userdata4.officePhone, userdata4.extension)
        self.assertEqual((user.permission == 1), "Not Authorized To Use This Command")
        self.assertTrue((user2.permission != 1), "Not Authorized To Use This Command")
        self.assertTrue((user3.permission != 1), "Not Authorized To Use This Command")
        self.assertTrue((user4.permission != 1), "Not Authorized To Use This Command")

        courseData = COURSE.objects.get(databaseID=645)
        course = COURSE.Course(courseData.databaseID, courseData.name, courseData.courseNumber, courseData.classNumber,
                               courseData.labList, courseData.time, courseData.location)
        self.assertEqual(Terminal.assignInstructorToCourse(course.databaseID, user.databaseID), user.firstName
                         + " " + user.lastName + " was added to " + course.name)
        self.assertEqual(Terminal.assignInstructorToCourse('234', user.databaseID), "Course not found")
        self.assertEqual(Terminal.assignInstructorToCourse(course.databaseID, '23'), "User not found")


    def test_assignAssistantToCourse(self):
        userdata = USER.objects.get(databaseID=69)
        user = User.User(userdata.permission, userdata.username, userdata.password,
                         userdata.databaseID, userdata.email, userdata.firstName,
                         userdata.lastName, userdata.contactPhone, userdata.officePhone, userdata.extension)
        userdata2 = USER.objects.get(databaseID=70)
        user2 = User.User(userdata2.permission, userdata2.username, userdata2.password,
                          userdata2.databaseID, userdata2.email, userdata2.firstName,
                          userdata2.lastName, userdata2.contactPhone, userdata2.officePhone, userdata2.extension)

        userdata3 = USER.objects.get(databaseID=71)
        user3 = User.User(userdata3.permission, userdata3.username, userdata3.password,
                          userdata3.databaseID, userdata3.email, userdata3.firstName,
                          userdata3.lastName, userdata3.contactPhone, userdata3.officePhone, userdata3.extension)
        userdata4 = USER.objects.get(databaseID=72)
        user4 = User.User(userdata4.permission, userdata4.username, userdata4.password,
                          userdata4.databaseID, userdata4.email, userdata4.firstName,
                          userdata4.lastName, userdata4.contactPhone, userdata4.officePhone, userdata4.extension)
        courseData = COURSE.objects.get(databaseID=645)
        course = COURSE.Course(courseData.databaseID, courseData.name, courseData.courseNumber, courseData.classNumber,
                               courseData.labList, courseData.time, courseData.location)
        courseData = COURSE.objects.get(databaseID=645)
        course = COURSE.Course(courseData.databaseID, courseData.name, courseData.courseNumber, courseData.classNumber,
                               courseData.labList, courseData.time, courseData.location)
        self.assertEqual((user.permission == 1), "Not Authorized To Use This Command")
        self.assertTrue((user2.permission != 1), "Not Authorized To Use This Command")
        self.assertTrue((user3.permission != 1), "Not Authorized To Use This Command")
        self.assertTrue((user4.permission != 1), "Not Authorized To Use This Command")
        self.assertEqual(Terminal.assignAssistantToCourse(course.databaseID, user.databaseID), user.firstName
                         + " " + user.lastName + " was added to " + course.name)
        self.assertEqual(Terminal.assignInstructorToCourse('234', user.databaseID), "Course not found")
        self.assertEqual(Terminal.assignInstructorToCourse(course.databaseID, '23'), "User not found")

    def test_viewCourseAssignments(self):

        userdata3 = USER.objects.get(databaseID=71)
        user3 = User.User(userdata3.permission, userdata3.username, userdata3.password,
                         userdata3.databaseID, userdata3.email, userdata3.firstName,
                         userdata3.lastName, userdata3.contactPhone, userdata3.officePhone, userdata3.extension)
        userdata4 = USER.objects.get(databaseID=72)
        user4 = User.User(userdata4.permission, userdata4.username, userdata4.password,
                          userdata4.databaseID, userdata4.email, userdata4.firstName,
                          userdata4.lastName, userdata4.contactPhone, userdata4.officePhone, userdata4.extension)

        courseData = COURSE.objects.get(databaseID=645)
        course = COURSE.Course(courseData.databaseID, courseData.name, courseData.courseNumber, courseData.classNumber,
                               courseData.labList, courseData.time, courseData.location)
        self.assertTrue(user3.permission == 3)
        self.assertTrue((user4.permission != 4), "Not Authorized To Use This Command")
        self.assertEqual(Terminal.viewCourseAssignments(userdata4.databaseID), "User is not an Instructor")
        self.assertEqual(Terminal.viewCourseAssignments(user3.databaseID), course.name)
        self.assertEqual(Terminal.viewCourseAssignments('1332'), "User not found" )
        self.assertEqual(Terminal.viewCourseAssignments('qakbd'), "Invalid UserId")

    def test_viewAssistantAssignments(self):
        userdata2 = USER.objects.get(databaseID=70)
        user2= User.User(userdata2.permission, userdata2.username, userdata2.password,
                         userdata2.databaseID, userdata2.email, userdata2.firstName,
                         userdata2.lastName, userdata2.contactPhone, userdata2.officePhone, userdata2.extension)

        userdata3 = USER.objects.get(databaseID=71)
        user3 = User.User(userdata3.permission, userdata3.username, userdata3.password,
                         userdata3.databaseID, userdata3.email, userdata3.firstName,
                         userdata3.lastName, userdata3.contactPhone, userdata3.officePhone, userdata3.extension)
        userdata4 = USER.objects.get(databaseID=72)
        user4 = User.User(userdata4.permission, userdata4.username, userdata4.password,
                         userdata4.databaseID, userdata4.email, userdata4.firstName,
                         userdata4.lastName, userdata4.contactPhone, userdata4.officePhone, userdata4.extension)
        courseData = COURSE.objects.get(databaseID=645)
        course = COURSE.Course(courseData.databaseID, courseData.name, courseData.courseNumber, courseData.classNumber,
                               courseData.labList, courseData.time, courseData.location)
        self.assertTrue(user4.permission == 4)
        self.assertTrue(user3.permission == 3)
        self.assertTrue((user2.permission != 4 | user2.permission != 3), "Not Authorized To Use This Command")
        self.assertEqual(Terminal.viewAssistantAssignments(userdata2.databaseID), "User is not a TA")
        self.assertEqual(Terminal.viewAssistantAssignments(user3.databaseID), "User is not a TA")
        self.assertEqual(Terminal.viewAssistantAssignments(user4.databaseID), course.name)
        self.assertEqual(Terminal.viewAssistantAssignments('1332'), "User not found")
        self.assertEqual(Terminal.viewAssistantAssignments('qakbd'), "Invalid UserId")

    def test_viewContactInfo(self):
        userdata = USER.objects.get(databaseID=69)
        user = User.User(3, userdata.username, userdata.password,
                         userdata.databaseID, userdata.email, userdata.firstName,
                         userdata.lastName, userdata.contactPhone, userdata.officePhone, userdata.extension)

        userdata2 = USER.objects.get(databaseID=70)
        user2 = User.User(userdata2.permission, userdata2.username, userdata2.password,
                          userdata2.databaseID, userdata2.email, userdata2.firstName,
                          userdata2.lastName, userdata2.contactPhone, userdata2.officePhone, userdata2.extension)

        userdata3 = USER.objects.get(databaseID=71)
        user3 = User.User(userdata3.permission, userdata3.username, userdata3.password,
                          userdata3.databaseID, userdata3.email, userdata3.firstName,
                          userdata3.lastName, userdata3.contactPhone, userdata3.officePhone, userdata3.extension)
        userdata4 = USER.objects.get(databaseID=72)
        user4 = User.User(userdata4.permission, userdata4.username, userdata4.password,
                          userdata4.databaseID, userdata4.email, userdata4.firstName,
                          userdata4.lastName, userdata4.contactPhone, userdata4.officePhone, userdata4.extension)

        self.assertEqual(Terminal.viewContactInfo(user.databaseID),user.permission + " " + user.username + " " + user.password
                         + " " + user.databaseID + " " + user.email + " " + user.firstName + " " + user.lastName + " " + user.contactPhone
                         + " " + user.officePhone + " " + user.extension)

        self.assertEqual(Terminal.viewContactInfo(user2.databaseID), user2.permission + " " + user2.username + " " + user2.password
                         + " " + user2.databaseID + " " + user2.email + " " + user2.firstName + " " + user2.lastName + " " + user2.contactPhone
                         + " " + user2.officePhone + " " + user2.extension)

        self.assertEqual(Terminal.viewContactInfo(user3.databaseID), user3.permission + " " + user3.username + " " + user3.password
                 + " " + user3.databaseID + " " + user3.email + " " + user3.firstName + " " + user3.lastName + " " + user3.contactPhone
                 + " " + user3.officePhone + " " +user3.extension)

        self.assertEqual(Terminal.viewContactInfo(user4.databaseID), user4.permission + " " + user4.username + " " + user4.password
                         + " " +  user4.databaseID + " " + user4.email + " " + user4.firstName + " " + user4.lastName + " " + user4.contactPhone
                         + " " + user4.officePhone + " " + user4.extension)

        self.assertEqual(Terminal.viewContactInfo('fvs'), "Invalid UserID")
        self.assertEqual(Terminal.viewContactInfo('234'), "User Not Found")
