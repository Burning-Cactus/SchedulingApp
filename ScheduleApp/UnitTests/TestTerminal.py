from django.test import TestCase
from myApp.models import *



class TestTerminal(TestCase):
    def setUp(self):
        # Populate USER table
        USER.objects.create(permission=[1], username="Wilton", password="wgdsg", email="woah@cool.com",
                            firstName="James", lastName="Franco", contactPhone="1112223333", officePhone="1112224444",
                            extension="123")
        USER.objects.create(permission=[2], username="BossBaby", password="slick", email="BossBaby@betterGmail.com",
                            firstName="Jenna", lastName="Flibarty", contactPhone="2223334444", officePhone="1231233333",
                            extension="149")
        USER.objects.create(permission=[3], username="plinko", password="Gruper", email="SHAMONA@jackson.com",
                            firstName="Richard", lastName="McCool", contactPhone="2228883333", officePhone="1234443333",
                            extension="324")
        USER.objects.create(permission=[4], username="Life", password="gordfge", email="LeafEricson@VikingMingle.com",
                            firstName="Leaf", lastName="Ericson", contactPhone="1114445555", officePhone="4443332222",
                            extension="151")
        USER.objects.create(permission=[1,3], username="jimbo", password="Fdf3e", email="POWER@rangers.com",
                            firstName="Linda", lastName="McCarthy", contactPhone="1234453423", officePhone="2345667777",
                            extension="123")
        USER.objects.create(permission=[1,4], username="justRandy", password="Randy", email="randy@randy.com",
                            firstName="Randy", lastName="Randerson", contactPhone="2223337565", officePhone="1234440000",
                            extension="3421")
        USER.objects.create(permission=[2,3], username="wat", password="UwU", email="OwO@animeCool.com",
                            firstName="Gregory", lastName="Spenderson", contactPhone="7778884444", officePhone="8883334444",
                            extension="7789")
        USER.objects.create(permission=[2,4], username="GoGo", password="willow", email="WhereAmI@FindYourself.com",
                            firstName="Membery", lastName="McFlenderson", contactPhone="4447778888", officePhone="2347775555",
                            extension="2453")

        # Populate COURSE Table
        COURSE.objects.create(name="Physics", courseNumber=342, classNumber=234,
                              time="7:00am-8:30am", location="PHY 324")
        COURSE.objects.create(name="Calculus", courseNumber=231, classNumber=432,
                              time="7:00am-8:30am", location="MATH 324")
        COURSE.objects.create(name="English", courseNumber=553, classNumber=342,
                              time="7:00am-8:30am", location="ENG 324")
        COURSE.objects.create(name="Art", courseNumber=456, classNumber=755,
                              time="7:00am-8:30am", location="ART 324")
        COURSE.objects.create(name="Music", courseNumber=675, classNumber=678,
                              time="7:00am-8:30am", location="MUS 324")

        # Populate LAB_SECTION Table
        LAB_SECTION.objects.create(name="Physics Lab", courseID=1, labNumber=765,
                                   time="4:00pm-6:00pm", location="PHY 345")
        LAB_SECTION.objects.create(name="Physics Lab", courseID=1, labNumber=743,
                                   time="4:00pm-6:00pm", location="PHY 342")
        LAB_SECTION.objects.create(name="Physics Lab", courseID=1, labNumber=967,
                                   time="4:00pm-6:00pm", location="PHY 457")
        LAB_SECTION.objects.create(name="Calculus Lab", courseID=2, labNumber=261,
                                   time="4:00pm-6:00pm", location="MATH 234")
        LAB_SECTION.objects.create(name="Calculus Lab", courseID=2, labNumber=643,
                                   time="4:00pm-6:00pm", location="MATH 345")
        LAB_SECTION.objects.create(name="Calculus Lab", courseID=2, labNumber=567,
                                   time="4:00pm-6:00pm", location="MATH 645")
        LAB_SECTION.objects.create(name="Art Lab", courseID=4, labNumber=453,
                                   time="4:00pm-6:00pm", location="ART 367")
        LAB_SECTION.objects.create(name="Art Lab", courseID=4, labNumber=473,
                                   time="4:00pm-6:00pm", location="ART 234")
        LAB_SECTION.objects.create(name="Music Lab", courseID=5, labNumber=956,
                                   time="4:00pm-6:00pm", location="MUS 345")
        LAB_SECTION.objects.create(name="Music Lab", courseID=5, labNumber=964,
                                   time="4:00pm-6:00pm", location="MUS 125")

        # Populate A_LIST Table
        A_LIST.objects.create(labID=1, assistantID=4)

        # Populate I_LIST Table
        I_LIST.objects.create(courseID=1, instructorID=3)

        # Instantiate the terminal
        self.TERMINAL = Terminal()

        # Create some helpful user data variables
        self.SUPERVISOR = USER.objects.get(id=1)
        self.ADMINISTRATOR = USER.objects.get(id=2)
        self.INSTRUCTOR = USER.objects.get(id=3)
        self.ASSISTANT = USER.objects.get(id=4)
        self.SUPER_INSTRUCTOR = USER.objects.get(id=5)
        self.SUPER_ASSISTANT = USER.objects.get(id=6)
        self.ADMIN_INSTRUCTOR = USER.objects.get(id=7)
        self.ADMIN_ASSISTANT = USER.objects.get(id=8)

        # Create some helpful course data variables
        self.PHYSICS = COURSE.objects.get(id=1)
        self.CALCULUS = COURSE.objects.get(id=2)
        self.ENGLISH = COURSE.objects.get(id=3)
        self.ART = COURSE.objects.get(id=4)
        self.MUSIC = COURSE.objects.get(id=5)

        # Create some helpful lab data variables
        self.LAB_PHYSICS = LAB_SECTION.objects.get(id=1)
        self.LAB_CALCULUS = LAB_SECTION.objects.get(id=4)
        self.LAB_ART = LAB_SECTION.objects.get(id=7)

    # Login Tests

    def testLogin(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.assertEqual(self.TERMINAL.user.username, self.SUPERVISOR.username)

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.assertEqual(self.TERMINAL.user.username, self.ADMINISTRATOR.username)

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.assertEqual(self.TERMINAL.user.username, self.INSTRUCTOR.username)

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.assertEqual(self.TERMINAL.user.username, self.ASSISTANT.username)

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.assertEqual(self.TERMINAL.user.username, self.SUPER_INSTRUCTOR.username)

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.assertEqual(self.TERMINAL.user.username, self.SUPER_ASSISTANT.username)

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.assertEqual(self.TERMINAL.user.username, self.ADMIN_INSTRUCTOR.username)

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.assertEqual(self.TERMINAL.user.username, self.ADMIN_ASSISTANT.username)

    def testLoginFail(self):
        # Invalid
        self.assertEqual("Invalid username or password", self.TERMINAL.login("bad", "data"))
        self.assertEqual("Invalid username or password", self.TERMINAL.login("bad", ""))
        self.assertEqual("Invalid username or password", self.TERMINAL.login("", "data"))
        self.assertEqual("Invalid username or password", self.TERMINAL.login("", ""))
        self.assertEqual("Invalid username or password", self.TERMINAL.login("Wilton", "data"))

        # Partially Valid
        self.assertEqual("Invalid username or password", self.TERMINAL.login("Wilton", ""))
        self.assertEqual("Invalid username or password", self.TERMINAL.login("", "slick"))

    # Logout Tests

    def testLogout(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.logout()
        self.assertEqual(self.TERMINAL.user, None)

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.TERMINAL.logout()
        self.assertEqual(self.TERMINAL.user, None)

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.logout()
        self.assertEqual(self.TERMINAL.user, None)

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.logout()
        self.assertEqual(self.TERMINAL.user, None)

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.logout()
        self.assertEqual(self.TERMINAL.user, None)

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.logout()
        self.assertEqual(self.TERMINAL.user, None)

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.logout()
        self.assertEqual(self.TERMINAL.user, None)

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.logout()
        self.assertEqual(self.TERMINAL.user, None)

    # Create Lab Tests

    def testCreateLab(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.createLab("Calculus Lab", "2", "100", "4:00pm-5:00pm", "MATH 345")
        self.assertEqual("Calculus Lab", LAB_SECTION.objects.get(labNumber="100", courseID="2").name)
        LAB_SECTION.objects.filter(labNumber="100", courseID="2").delete()

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.TERMINAL.createLab("Calculus Lab", "2", "100", "4:00pm-5:00pm", "MATH 345")
        self.assertEqual("Calculus Lab", LAB_SECTION.objects.get(labNumber="100", courseID="2").name)
        LAB_SECTION.objects.filter(labNumber="100", courseID="2").delete()

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.createLab("Calculus Lab", "2", "100", "4:00pm-5:00pm", "MATH 345")
        self.assertEqual(0, len(LAB_SECTION.objects.filter(labNumber="100", courseID="2")))

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.createLab("Calculus Lab", "2", "100", "4:00pm-5:00pm", "MATH 345")
        self.assertEqual(0, len(LAB_SECTION.objects.filter(labNumber="100", courseID="2")))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.createLab("Calculus Lab", "2", "100", "4:00pm-5:00pm", "MATH 345")
        self.assertEqual("Calculus Lab", LAB_SECTION.objects.get(labNumber="100", courseID="2").name)
        LAB_SECTION.objects.filter(labNumber="100", courseID="2").delete()

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.createLab("Calculus Lab", "2", "100", "4:00pm-5:00pm", "MATH 345")
        self.assertEqual("Calculus Lab", LAB_SECTION.objects.get(labNumber="100", courseID="2").name)
        LAB_SECTION.objects.filter(labNumber="100", courseID="2").delete()


        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.createLab("Calculus Lab", "2", "100", "4:00pm-5:00pm", "MATH 345")
        self.assertEqual("Calculus Lab", LAB_SECTION.objects.get(labNumber="100", courseID="2").name)
        LAB_SECTION.objects.filter(labNumber="100", courseID="2").delete()


        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.createLab("Calculus Lab", "2", "100", "4:00pm-5:00pm", "MATH 345")
        self.assertEqual("Calculus Lab", LAB_SECTION.objects.get(labNumber="100", courseID="2").name)
        LAB_SECTION.objects.filter(labNumber="100", courseID="2").delete()


    def testCreateLabWithConflictingLabNumber(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "2", self.LAB_CALCULUS.labNumber, "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.assertEqual(None,
                         self.TERMINAL.createLab("Calculus Lab", "2", self.LAB_CALCULUS.labNumber, "4:00pm-6:00pm",
                                                 "MATH 231"))

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.assertEqual(None,
                         self.TERMINAL.createLab("Calculus Lab", "2", self.LAB_CALCULUS.labNumber, "4:00pm-6:00pm",
                                                 "MATH 231"))

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.assertEqual(None,
                         self.TERMINAL.createLab("Calculus Lab", "2", self.LAB_CALCULUS.labNumber, "4:00pm-6:00pm",
                                                 "MATH 231"))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.assertEqual(None,
                         self.TERMINAL.createLab("Calculus Lab", "2", self.LAB_CALCULUS.labNumber, "4:00pm-6:00pm",
                                                 "MATH 231"))

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.assertEqual(None,
                         self.TERMINAL.createLab("Calculus Lab", "2", self.LAB_CALCULUS.labNumber, "4:00pm-6:00pm",
                                                 "MATH 231"))

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.assertEqual(None,
                         self.TERMINAL.createLab("Calculus Lab", "2", self.LAB_CALCULUS.labNumber, "4:00pm-6:00pm",
                                                 "MATH 231"))

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.assertEqual(None,
                         self.TERMINAL.createLab("Calculus Lab", "2", self.LAB_CALCULUS.labNumber, "4:00pm-6:00pm",
                                                 "MATH 231"))

    def testCreateLabCourseDoesNotExist(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.assertEqual(None,
                         self.TERMINAL.createLab("Calculus Lab", "500", "100", "4:00pm-6:00pm",
                                                 "MATH 231"))

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.assertEqual(None,
                         self.TERMINAL.createLab("Calculus Lab", "500", "100", "4:00pm-6:00pm",
                                                 "MATH 231"))

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.assertEqual(None,
                         self.TERMINAL.createLab("Calculus Lab", "500", "100", "4:00pm-6:00pm",
                                                 "MATH 231"))

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.assertEqual(None,
                         self.TERMINAL.createLab("Calculus Lab", "500", "100", "4:00pm-6:00pm",
                                                 "MATH 231"))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.assertEqual(None,
                         self.TERMINAL.createLab("Calculus Lab", "500", "100", "4:00pm-6:00pm",
                                                 "MATH 231"))

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.assertEqual(None,
                         self.TERMINAL.createLab("Calculus Lab", "500", "100", "4:00pm-6:00pm",
                                                 "MATH 231"))

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.assertEqual(None,
                         self.TERMINAL.createLab("Calculus Lab", "500", "100", "4:00pm-6:00pm",
                                                 "MATH 231"))

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.assertEqual(None,
                         self.TERMINAL.createLab("Calculus Lab", "500", "100", "4:00pm-6:00pm",
                                                 "MATH 231"))

    def testCreateLabCourseIsNONE(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", None, "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", None, "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", None, "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", None, "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", None, "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", None, "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", None, "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", None, "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

    def testCreateLabMissingInput(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.assertEqual(None, self.TERMINAL.createLab("", "2", "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.assertEqual(None, self.TERMINAL.createLab("", "2", "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.assertEqual(None, self.TERMINAL.createLab("", "2", "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.assertEqual(None, self.TERMINAL.createLab("", "2", "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.assertEqual(None, self.TERMINAL.createLab("", "2", "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.assertEqual(None, self.TERMINAL.createLab("", "2", "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.assertEqual(None, self.TERMINAL.createLab("", "2", "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.assertEqual(None, self.TERMINAL.createLab("", "2", "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "", "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "", "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "", "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "", "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "", "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "", "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "", "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "", "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "2", "", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "2", "", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "2", "", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "2", "", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "2", "", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "2", "", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "2", "", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "2", "", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "2", "100", "",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "2", "100", "",
                                                       "MATH 231"))

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "2", "100", "",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "2", "100", "",
                                                       "MATH 231"))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "2", "100", "",
                                                       "MATH 231"))

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "2", "100", "",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "2", "100", "",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "2", "100", "",
                                                       "MATH 231"))

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "2", "100", "4:00pm-6:00pm",
                                                       ""))

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "2", "100", "4:00pm-6:00pm",
                                                       ""))

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "2", "100", "4:00pm-6:00pm",
                                                       ""))

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "2", "100", "4:00pm-6:00pm",
                                                       ""))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "2", "100", "4:00pm-6:00pm",
                                                       ""))

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "2", "100", "4:00pm-6:00pm",
                                                       ""))

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "2", "100", "4:00pm-6:00pm",
                                                       ""))

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.assertEqual(None, self.TERMINAL.createLab("Calculus Lab", "2", "100", "4:00pm-6:00pm",
                                                       ""))

    # Edit Lab Tests

    def testEditLab(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, self.LAB_CALCULUS.name, self.LAB_CALCULUS.courseID,
                              self.LAB_CALCULUS.labNumber, "", "MATH 900")
        self.assertEqual("MATH 900", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location)
        self.assertEqual(self.LAB_CALCULUS.time, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).time)
        # reset location value to what it was before edit
        LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location = self.LAB_CALCULUS.location

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, self.LAB_CALCULUS.name, self.LAB_CALCULUS.courseID,
                              self.LAB_CALCULUS.labNumber, "", "MATH 900")
        self.assertEqual("MATH 900", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location)
        # reset location value to what it was before edit
        LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location = self.LAB_CALCULUS.location

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, self.LAB_CALCULUS.name, self.LAB_CALCULUS.courseID,
                              self.LAB_CALCULUS.labNumber, "", "MATH 900")
        self.assertEqual(self.LAB_CALCULUS.location, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id))

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, self.LAB_CALCULUS.name, self.LAB_CALCULUS.courseID,
                              self.LAB_CALCULUS.labNumber, "", "MATH 900")
        self.assertEqual(self.LAB_CALCULUS.location, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, self.LAB_CALCULUS.name, self.LAB_CALCULUS.courseID,
                              self.LAB_CALCULUS.labNumber, "", "MATH 900")
        self.assertEqual("MATH 900", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location)
        # reset location value to what it was before edit
        LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location = self.LAB_CALCULUS.location

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, self.LAB_CALCULUS.name, self.LAB_CALCULUS.courseID,
                              self.LAB_CALCULUS.labNumber, "", "MATH 900")
        self.assertEqual("MATH 900", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location)
        # reset location value to what it was before edit
        LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location = self.LAB_CALCULUS.location

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, self.LAB_CALCULUS.name, self.LAB_CALCULUS.courseID,
                              self.LAB_CALCULUS.labNumber, "", "MATH 900")
        self.assertEqual("MATH 900", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location)
        # reset location value to what it was before edit
        LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location = self.LAB_CALCULUS.location

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, self.LAB_CALCULUS.name, self.LAB_CALCULUS.courseID,
                              self.LAB_CALCULUS.labNumber, "", "MATH 900")
        self.assertEqual("MATH 900", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location)
        # reset location value to what it was before edit
        LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location = self.LAB_CALCULUS.location

    def testEditLabCourseDoesNotExist(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, self.LAB_CALCULUS.name, "500",
                              self.LAB_CALCULUS.labNumber, self.LAB_CALCULUS.time, self.LAB_CALCULUS.location)
        self.assertEqual(self.LAB_CALCULUS.courseID, "2")

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, self.LAB_CALCULUS.name, "500",
                              self.LAB_CALCULUS.labNumber, self.LAB_CALCULUS.time, self.LAB_CALCULUS.location)
        self.assertEqual(self.LAB_CALCULUS.courseID, "2")

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, self.LAB_CALCULUS.name, "500",
                              self.LAB_CALCULUS.labNumber, self.LAB_CALCULUS.time, self.LAB_CALCULUS.location)
        self.assertEqual(self.LAB_CALCULUS.courseID, "2")

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, self.LAB_CALCULUS.name, "500",
                              self.LAB_CALCULUS.labNumber, self.LAB_CALCULUS.time, self.LAB_CALCULUS.location)
        self.assertEqual(self.LAB_CALCULUS.courseID, "2")

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, self.LAB_CALCULUS.name, "500",
                              self.LAB_CALCULUS.labNumber, self.LAB_CALCULUS.time, self.LAB_CALCULUS.location)
        self.assertEqual(self.LAB_CALCULUS.courseID, "2")

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, self.LAB_CALCULUS.name, "500",
                              self.LAB_CALCULUS.labNumber, self.LAB_CALCULUS.time, self.LAB_CALCULUS.location)
        self.assertEqual(self.LAB_CALCULUS.courseID, "2")

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, self.LAB_CALCULUS.name, "500",
                              self.LAB_CALCULUS.labNumber, self.LAB_CALCULUS.time, self.LAB_CALCULUS.location)
        self.assertEqual(self.LAB_CALCULUS.courseID, "2")

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, self.LAB_CALCULUS.name, "500",
                              self.LAB_CALCULUS.labNumber, self.LAB_CALCULUS.time, self.LAB_CALCULUS.location)
        self.assertEqual(self.LAB_CALCULUS.courseID, "2")


    def testEditLabConflictingLabNumber(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, self.LAB_CALCULUS.name, self.LAB_CALCULUS.courseID,
                              "643", self.LAB_CALCULUS.time, self.LAB_CALCULUS.location)
        self.assertEqual(self.LAB_CALCULUS.labNumber, "261")

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, self.LAB_CALCULUS.name, self.LAB_CALCULUS.courseID,
                              "643", self.LAB_CALCULUS.time, self.LAB_CALCULUS.location)
        self.assertEqual(self.LAB_CALCULUS.labNumber, "261")

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, self.LAB_CALCULUS.name, self.LAB_CALCULUS.courseID,
                              "643", self.LAB_CALCULUS.time, self.LAB_CALCULUS.location)
        self.assertEqual(self.LAB_CALCULUS.labNumber, "261")

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, self.LAB_CALCULUS.name, self.LAB_CALCULUS.courseID,
                              "643", self.LAB_CALCULUS.time, self.LAB_CALCULUS.location)
        self.assertEqual(self.LAB_CALCULUS.labNumber, "261")

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, self.LAB_CALCULUS.name, self.LAB_CALCULUS.courseID,
                              "643", self.LAB_CALCULUS.time, self.LAB_CALCULUS.location)
        self.assertEqual(self.LAB_CALCULUS.labNumber, "261")

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, self.LAB_CALCULUS.name, self.LAB_CALCULUS.courseID,
                              "643", self.LAB_CALCULUS.time, self.LAB_CALCULUS.location)
        self.assertEqual(self.LAB_CALCULUS.labNumber, "261")

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, self.LAB_CALCULUS.name, self.LAB_CALCULUS.courseID,
                              "643", self.LAB_CALCULUS.time, self.LAB_CALCULUS.location)
        self.assertEqual(self.LAB_CALCULUS.labNumber, "261")

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, self.LAB_CALCULUS.name, self.LAB_CALCULUS.courseID,
                              "643", self.LAB_CALCULUS.time, self.LAB_CALCULUS.location)
        self.assertEqual(self.LAB_CALCULUS.labNumber, "261")

    def testEditLabLabIdIsNone(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.editLab(None, self.LAB_CALCULUS.name, self.LAB_CALCULUS.courseID,
                              self.LAB_CALCULUS.labNumber, self.LAB_CALCULUS.time, "MATH 9000")
        self.assertEqual(self.LAB_CALCULUS.location, "MATH 234")

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.TERMINAL.editLab(None, self.LAB_CALCULUS.name, self.LAB_CALCULUS.courseID,
                              self.LAB_CALCULUS.labNumber, self.LAB_CALCULUS.time, "MATH 9000")
        self.assertEqual(self.LAB_CALCULUS.location, "MATH 234")

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.editLab(None, self.LAB_CALCULUS.name, self.LAB_CALCULUS.courseID,
                              self.LAB_CALCULUS.labNumber, self.LAB_CALCULUS.time, "MATH 9000")
        self.assertEqual(self.LAB_CALCULUS.location, "MATH 234")

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.editLab(None, self.LAB_CALCULUS.name, self.LAB_CALCULUS.courseID,
                              self.LAB_CALCULUS.labNumber, self.LAB_CALCULUS.time, "MATH 9000")
        self.assertEqual(self.LAB_CALCULUS.location, "MATH 234")

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.editLab(None, self.LAB_CALCULUS.name, self.LAB_CALCULUS.courseID,
                              self.LAB_CALCULUS.labNumber, self.LAB_CALCULUS.time, "MATH 9000")
        self.assertEqual(self.LAB_CALCULUS.location, "MATH 234")

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.editLab(None, self.LAB_CALCULUS.name, self.LAB_CALCULUS.courseID,
                              self.LAB_CALCULUS.labNumber, self.LAB_CALCULUS.time, "MATH 9000")
        self.assertEqual(self.LAB_CALCULUS.location, "MATH 234")

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.editLab(None, self.LAB_CALCULUS.name, self.LAB_CALCULUS.courseID,
                              self.LAB_CALCULUS.labNumber, self.LAB_CALCULUS.time, "MATH 9000")
        self.assertEqual(self.LAB_CALCULUS.location, "MATH 234")

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.editLab(None, self.LAB_CALCULUS.name, self.LAB_CALCULUS.courseID,
                              self.LAB_CALCULUS.labNumber, self.LAB_CALCULUS.time, "MATH 9000")
        self.assertEqual(self.LAB_CALCULUS.location, "MATH 234")

    def testEditLabDoNotEditFields(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.editLab("", "Another Name", "", "", "", "")
        self.assertEqual("Another Name", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).name)
        self.assertEqual(self.LAB_CALCULUS.courseID, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).courseID)
        self.assertEqual(self.LAB_CALCULUS.labNumber, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).labNumber)
        self.assertEqual(self.LAB_CALCULUS.time, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).time)
        self.assertEqual(self.LAB_CALCULUS.location, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location)
        # reset location value to what it was before edit
        LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).name = self.LAB_CALCULUS.name

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.TERMINAL.editLab("", "Another Name", "", "", "", "")
        self.assertEqual("Another Name", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).name)
        self.assertEqual(self.LAB_CALCULUS.courseID, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).courseID)
        self.assertEqual(self.LAB_CALCULUS.labNumber, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).labNumber)
        self.assertEqual(self.LAB_CALCULUS.time, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).time)
        self.assertEqual(self.LAB_CALCULUS.location, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location)
        # reset location value to what it was before edit
        LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).name = self.LAB_CALCULUS.name

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.editLab("", "Another Name", "", "", "", "")
        self.assertEqual("Another Name", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).name)
        self.assertEqual(self.LAB_CALCULUS.courseID, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).courseID)
        self.assertEqual(self.LAB_CALCULUS.labNumber, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).labNumber)
        self.assertEqual(self.LAB_CALCULUS.time, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).time)
        self.assertEqual(self.LAB_CALCULUS.location, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location)
        # reset location value to what it was before edit
        LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).name = self.LAB_CALCULUS.name

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.editLab("", "Another Name", "", "", "", "")
        self.assertEqual("Another Name", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).name)
        self.assertEqual(self.LAB_CALCULUS.courseID, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).courseID)
        self.assertEqual(self.LAB_CALCULUS.labNumber, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).labNumber)
        self.assertEqual(self.LAB_CALCULUS.time, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).time)
        self.assertEqual(self.LAB_CALCULUS.location, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location)
        # reset location value to what it was before edit
        LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).name = self.LAB_CALCULUS.name

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.editLab("", "Another Name", "", "", "", "")
        self.assertEqual("Another Name", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).name)
        self.assertEqual(self.LAB_CALCULUS.courseID, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).courseID)
        self.assertEqual(self.LAB_CALCULUS.labNumber, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).labNumber)
        self.assertEqual(self.LAB_CALCULUS.time, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).time)
        self.assertEqual(self.LAB_CALCULUS.location, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location)
        # reset location value to what it was before edit
        LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).name = self.LAB_CALCULUS.name

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.editLab("", "Another Name", "", "", "", "")
        self.assertEqual("Another Name", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).name)
        self.assertEqual(self.LAB_CALCULUS.courseID, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).courseID)
        self.assertEqual(self.LAB_CALCULUS.labNumber, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).labNumber)
        self.assertEqual(self.LAB_CALCULUS.time, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).time)
        self.assertEqual(self.LAB_CALCULUS.location, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location)
        # reset location value to what it was before edit
        LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).name = self.LAB_CALCULUS.name

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.editLab("", "Another Name", "", "", "", "")
        self.assertEqual("Another Name", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).name)
        self.assertEqual(self.LAB_CALCULUS.courseID, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).courseID)
        self.assertEqual(self.LAB_CALCULUS.labNumber, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).labNumber)
        self.assertEqual(self.LAB_CALCULUS.time, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).time)
        self.assertEqual(self.LAB_CALCULUS.location, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location)
        # reset location value to what it was before edit
        LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).name = self.LAB_CALCULUS.name

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.editLab("", "Another Name", "", "", "", "")
        self.assertEqual("Another Name", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).name)
        self.assertEqual(self.LAB_CALCULUS.courseID, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).courseID)
        self.assertEqual(self.LAB_CALCULUS.labNumber, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).labNumber)
        self.assertEqual(self.LAB_CALCULUS.time, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).time)
        self.assertEqual(self.LAB_CALCULUS.location, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location)
        # reset location value to what it was before edit
        LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).name = self.LAB_CALCULUS.name

    def testEditLabWithAssistant(self):
        pass

    # Delete Lab Tests

    def testDeleteLab(self):
        pass

    def testDeleteLabWithAssistants(self):
        pass

    # Create Course Tests

    def testCreateCourse(self):
        pass

    def testCreateCourseDuplicate(self):
        pass

    def testCreateCourseMissingInput(self):
        pass

    # Edit Course Tests

    def testEditCourse(self):
        pass

    def testEditCourseToProduceDuplicate(self):
        pass

    def testEditCourseProduceMissingFields(self):
        pass

    def editCourseWithLabs(self):
        pass

    def editCourseWithInstructorsAndAssistants(self):
        pass

    # Delete Course Tests

    def testDeleteCourse(self):
        pass

    def testDeleteCourseWithInstructorsAndAssistants(self):
        pass

    def testDeleteCourseWithLabs(self):
        pass

    # Create Account Tests

    def testCreateAccount(self):
        pass

    def testCreateAccountDuplicate(self):
        pass

    def testCreateAccountMissingInput(self):
        pass

    # Edit Account Tests

    def testEditAccount(self):
        pass

    def testEditAccountToProduceDuplicate(self):
        pass

    def testEditAccountToMissingData(self):
        pass

    # Delete Account Tests

    def testDeleteAccountWithoutCascade(self):
        pass

    def testDeleteInstructorWithCourses(self):
        pass

    def testDeleteAssistantWithCourses(self):
        pass

    def testDeleteAssistantWithLabSections(self):
        pass

    # Email Tests

    def testEmail(self):
        pass

    # Accesss Data Tests

    def testAccessData(self):
        pass

    # Assign Instructor to Course Tests

    def testAssignInstructorToCourse(self):
        pass

    def testAssignInstructorToCourseInstructorDoesNotExist(self):
        pass

    def testAssignInstructorToCourseUserIsNotInstructor(self):
        pass

    def testAssignInstructorToCourseCourseDoesNotExist(self):
        pass

    def testAssignInstructorToCourseInstructorAlreadyAssigned(self):
        pass

    # Assign Assistant to Course Tests

    def testAssignAssistantToCourse(self):
        pass

    def testAssignAssistantToCourseAssistantDoesNotExist(self):
        pass

    def testAssignAssistantToCourseUserIsNotAssistant(self):
        pass

    def testAssignAssistantToCourseCourseDoesNotExist(self):
        pass

    def testAssignAssistantToCourseAssistantAlreadyAssigned(self):
        pass

    # Assign Assistant to Lab Tests

    def testAssignAssistantToLab(self):
        pass

    def testAssignAssistantToLabAssistantDoesNotExist(self):
        pass

    def testAssignAssistantToLabUserIsNotAssistant(self):
        pass

    def testAssignAssistantToLabLabDoesNotExist(self):
        pass

    def testAssignAssistantToLabAssistantAlreadyAssigned(self):
        pass

    # View Course Assignments Tests

    def testViewCourseAssignments(self):
        pass

    # View Assistant Assignemnts Tests

    def testViewAssisntantAssignments(self):
        pass

    # View Contact Info Tests

    def testViewContactInfo(self):
        pass








