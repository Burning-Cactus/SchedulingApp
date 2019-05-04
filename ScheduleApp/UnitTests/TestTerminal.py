from django.test import TestCase
from myApp.models import *



class TestTerminal(TestCase):
    def setUp(self):
        # Populate USER table
        USER.objects.create(permission=[1], username="Wilton", password="wgdsg", email="woah@cool.com",
                            firstName="James", lastName="Franco", contactPhone="1112223333", officePhone="1112224444",
                            extension="123").save()
        USER.objects.create(permission=[2], username="BossBaby", password="slick", email="BossBaby@betterGmail.com",
                            firstName="Jenna", lastName="Flibarty", contactPhone="2223334444", officePhone="1231233333",
                            extension="149").save()
        USER.objects.create(permission=[3], username="plinko", password="Gruper", email="SHAMONA@jackson.com",
                            firstName="Richard", lastName="McCool", contactPhone="2228883333", officePhone="1234443333",
                            extension="324").save()
        USER.objects.create(permission=[4], username="Life", password="gordfge", email="LeafEricson@VikingMingle.com",
                            firstName="Leaf", lastName="Ericson", contactPhone="1114445555", officePhone="4443332222",
                            extension="151").save()
        USER.objects.create(permission=[1,3], username="jimbo", password="Fdf3e", email="POWER@rangers.com",
                            firstName="Linda", lastName="McCarthy", contactPhone="1234453423", officePhone="2345667777",
                            extension="123").save()
        USER.objects.create(permission=[1,4], username="justRandy", password="Randy", email="randy@randy.com",
                            firstName="Randy", lastName="Randerson", contactPhone="2223337565", officePhone="1234440000",
                            extension="3421").save()
        USER.objects.create(permission=[2,3], username="wat", password="UwU", email="OwO@animeCool.com",
                            firstName="Gregory", lastName="Spenderson", contactPhone="7778884444", officePhone="8883334444",
                            extension="7789").save()
        USER.objects.create(permission=[2,4], username="GoGo", password="willow", email="WhereAmI@FindYourself.com",
                            firstName="Membery", lastName="McFlenderson", contactPhone="4447778888", officePhone="2347775555",
                            extension="2453").save()

        # Populate COURSE Table
        COURSE.objects.create(name="Physics", courseNumber=342, classNumber=234,
                              time="7:00am-8:30am", location="PHY 324").save()
        COURSE.objects.create(name="Calculus", courseNumber=231, classNumber=432,
                              time="7:00am-8:30am", location="MATH 324").save()
        COURSE.objects.create(name="English", courseNumber=553, classNumber=342,
                              time="7:00am-8:30am", location="ENG 324").save()
        COURSE.objects.create(name="Art", courseNumber=456, classNumber=755,
                              time="7:00am-8:30am", location="ART 324").save()
        COURSE.objects.create(name="Music", courseNumber=675, classNumber=678,
                              time="7:00am-8:30am", location="MUS 324").save()

        # Populate LAB_SECTION Table
        LAB_SECTION.objects.create(name="Physics Lab", courseID=1, labNumber=765,
                                   time="4:00pm-6:00pm", location="PHY 345").save()
        LAB_SECTION.objects.create(name="Physics Lab", courseID=1, labNumber=743,
                                   time="4:00pm-6:00pm", location="PHY 342").save()
        LAB_SECTION.objects.create(name="Physics Lab", courseID=1, labNumber=967,
                                   time="4:00pm-6:00pm", location="PHY 457").save()
        LAB_SECTION.objects.create(name="Calculus Lab", courseID=2, labNumber=261,
                                   time="4:00pm-6:00pm", location="MATH 234").save()
        LAB_SECTION.objects.create(name="Calculus Lab", courseID=2, labNumber=643,
                                   time="4:00pm-6:00pm", location="MATH 345").save()
        LAB_SECTION.objects.create(name="Calculus Lab", courseID=2, labNumber=567,
                                   time="4:00pm-6:00pm", location="MATH 645").save()
        LAB_SECTION.objects.create(name="Art Lab", courseID=4, labNumber=453,
                                   time="4:00pm-6:00pm", location="ART 367").save()
        LAB_SECTION.objects.create(name="Art Lab", courseID=4, labNumber=473,
                                   time="4:00pm-6:00pm", location="ART 234").save()
        LAB_SECTION.objects.create(name="Music Lab", courseID=5, labNumber=956,
                                   time="4:00pm-6:00pm", location="MUS 345").save()
        LAB_SECTION.objects.create(name="Music Lab", courseID=5, labNumber=964,
                                   time="4:00pm-6:00pm", location="MUS 125").save()

        # Populate A_LIST Table
        A_LIST.objects.create(labID=1, assistantID=4).save()

        # Populate I_LIST Table
        I_LIST.objects.create(courseID=1, instructorID=3).save()

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
        lab = LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id)
        lab.location = self.LAB_CALCULUS.location
        lab.save()

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, self.LAB_CALCULUS.name, self.LAB_CALCULUS.courseID,
                              self.LAB_CALCULUS.labNumber, "", "MATH 900")
        self.assertEqual("MATH 900", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location)
        # reset location value to what it was before edit
        lab = LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id)
        lab.location = self.LAB_CALCULUS.location
        lab.save()

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
        lab = LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id)
        lab.location = self.LAB_CALCULUS.location
        lab.save()

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, self.LAB_CALCULUS.name, self.LAB_CALCULUS.courseID,
                              self.LAB_CALCULUS.labNumber, "", "MATH 900")
        self.assertEqual("MATH 900", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location)
        # reset location value to what it was before edit
        lab = LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id)
        lab.location = self.LAB_CALCULUS.location
        lab.save()

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, self.LAB_CALCULUS.name, self.LAB_CALCULUS.courseID,
                              self.LAB_CALCULUS.labNumber, "", "MATH 900")
        self.assertEqual("MATH 900", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location)
        # reset location value to what it was before edit
        lab = LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id)
        lab.location = self.LAB_CALCULUS.location
        lab.save()

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, self.LAB_CALCULUS.name, self.LAB_CALCULUS.courseID,
                              self.LAB_CALCULUS.labNumber, "", "MATH 900")
        self.assertEqual("MATH 900", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location)
        # reset location value to what it was before edit
        lab = LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id)
        lab.location = self.LAB_CALCULUS.location
        lab.save()

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
        lab = LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id)
        lab.name = self.LAB_CALCULUS.name
        lab.save()

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.TERMINAL.editLab("", "Another Name", "", "", "", "")
        self.assertEqual("Another Name", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).name)
        self.assertEqual(self.LAB_CALCULUS.courseID, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).courseID)
        self.assertEqual(self.LAB_CALCULUS.labNumber, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).labNumber)
        self.assertEqual(self.LAB_CALCULUS.time, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).time)
        self.assertEqual(self.LAB_CALCULUS.location, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location)
        # reset location value to what it was before edit
        lab = LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id)
        lab.name = self.LAB_CALCULUS.name
        lab.save()

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.editLab("", "Another Name", "", "", "", "")
        self.assertEqual("Another Name", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).name)
        self.assertEqual(self.LAB_CALCULUS.courseID, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).courseID)
        self.assertEqual(self.LAB_CALCULUS.labNumber, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).labNumber)
        self.assertEqual(self.LAB_CALCULUS.time, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).time)
        self.assertEqual(self.LAB_CALCULUS.location, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location)
        self.assertEqual(self.LAB_CALCULUS.name, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id))

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.editLab("", "Another Name", "", "", "", "")
        self.assertEqual("Another Name", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).name)
        self.assertEqual(self.LAB_CALCULUS.courseID, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).courseID)
        self.assertEqual(self.LAB_CALCULUS.labNumber, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).labNumber)
        self.assertEqual(self.LAB_CALCULUS.time, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).time)
        self.assertEqual(self.LAB_CALCULUS.location, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location)
        self.assertEqual(self.LAB_CALCULUS.name, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.editLab("", "Another Name", "", "", "", "")
        self.assertEqual("Another Name", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).name)
        self.assertEqual(self.LAB_CALCULUS.courseID, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).courseID)
        self.assertEqual(self.LAB_CALCULUS.labNumber, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).labNumber)
        self.assertEqual(self.LAB_CALCULUS.time, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).time)
        self.assertEqual(self.LAB_CALCULUS.location, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location)
        # reset location value to what it was before edit
        lab = LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id)
        lab.name = self.LAB_CALCULUS.name
        lab.save()

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.editLab("", "Another Name", "", "", "", "")
        self.assertEqual("Another Name", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).name)
        self.assertEqual(self.LAB_CALCULUS.courseID, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).courseID)
        self.assertEqual(self.LAB_CALCULUS.labNumber, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).labNumber)
        self.assertEqual(self.LAB_CALCULUS.time, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).time)
        self.assertEqual(self.LAB_CALCULUS.location, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location)
        # reset location value to what it was before edit
        lab = LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id)
        lab.name = self.LAB_CALCULUS.name
        lab.save()

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.editLab("", "Another Name", "", "", "", "")
        self.assertEqual("Another Name", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).name)
        self.assertEqual(self.LAB_CALCULUS.courseID, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).courseID)
        self.assertEqual(self.LAB_CALCULUS.labNumber, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).labNumber)
        self.assertEqual(self.LAB_CALCULUS.time, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).time)
        self.assertEqual(self.LAB_CALCULUS.location, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location)
        # reset location value to what it was before edit
        lab = LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id)
        lab.name = self.LAB_CALCULUS.name
        lab.save()

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.editLab("", "Another Name", "", "", "", "")
        self.assertEqual("Another Name", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).name)
        self.assertEqual(self.LAB_CALCULUS.courseID, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).courseID)
        self.assertEqual(self.LAB_CALCULUS.labNumber, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).labNumber)
        self.assertEqual(self.LAB_CALCULUS.time, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).time)
        self.assertEqual(self.LAB_CALCULUS.location, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location)
        # reset location value to what it was before edit
        lab = LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id)
        lab.name = self.LAB_CALCULUS.name
        lab.save()

    def testEditLabCourseFieldWithAssistant(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        A_LIST.objects.create(assistantID=self.ASSISTANT.id, labID=self.LAB_CALCULUS.id).save()
        self.TERMINAL.editLab("", "", "1", "", "", "")
        self.assertEqual("1", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).courseID)
        self.assertEqual(0, len(A_LIST.objects.filter(assistantID=self.ASSISTANT.id)))

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        A_LIST.objects.create(assistantID=self.ASSISTANT.id, labID=self.LAB_CALCULUS.id).save()
        self.TERMINAL.editLab("", "", "1", "", "", "")
        self.assertEqual("1", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).courseID)
        self.assertEqual(0, len(A_LIST.objects.filter(assistantID=self.ASSISTANT.id)))

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        A_LIST.objects.create(assistantID=self.ASSISTANT.id, labID=self.LAB_CALCULUS.id).save()
        self.TERMINAL.editLab("", "", "1", "", "", "")
        self.assertEqual("2", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).courseID)
        self.assertEqual(1, len(A_LIST.objects.filter(assistantID=self.ASSISTANT.id)))
        A_LIST.objects.get(assistantID=self.ASSISTANT.id).delete()

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        A_LIST.objects.create(assistantID=self.ASSISTANT.id, labID=self.LAB_CALCULUS.id).save()
        self.TERMINAL.editLab("", "", "1", "", "", "")
        self.assertEqual("2", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).courseID)
        self.assertEqual(1, len(A_LIST.objects.filter(assistantID=self.ASSISTANT.id)))
        A_LIST.objects.get(assistantID=self.ASSISTANT.id).delete()

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        A_LIST.objects.create(assistantID=self.ASSISTANT.id, labID=self.LAB_CALCULUS.id).save()
        self.TERMINAL.editLab("", "", "1", "", "", "")
        self.assertEqual("1", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).courseID)
        self.assertEqual(0, len(A_LIST.objects.filter(assistantID=self.ASSISTANT.id)))

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        A_LIST.objects.create(assistantID=self.ASSISTANT.id, labID=self.LAB_CALCULUS.id).save()
        self.TERMINAL.editLab("", "", "1", "", "", "")
        self.assertEqual("1", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).courseID)
        self.assertEqual(0, len(A_LIST.objects.filter(assistantID=self.ASSISTANT.id)))

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        A_LIST.objects.create(assistantID=self.ASSISTANT.id, labID=self.LAB_CALCULUS.id).save()
        self.TERMINAL.editLab("", "", "1", "", "", "")
        self.assertEqual("1", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).courseID)
        self.assertEqual(0, len(A_LIST.objects.filter(assistantID=self.ASSISTANT.id)))

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        A_LIST.objects.create(assistantID=self.ASSISTANT.id, labID=self.LAB_CALCULUS.id).save()
        self.TERMINAL.editLab("", "", "1", "", "", "")
        self.assertEqual("1", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).courseID)
        self.assertEqual(0, len(A_LIST.objects.filter(assistantID=self.ASSISTANT.id)))


    # Delete Lab Tests

    def testDeleteLab(self):
        labToDelete = LAB_SECTION.objects.create(name="Music Lab", courseID=5, labNumber=334,
                                                 time="4:00pm-6:00pm", location="MUS 125")
        labToDelete.save()

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        A_LIST.objects.create(assistantID=self.ASSISTANT.id, labID=labToDelete.id).save()
        self.TERMINAL.deleteLab(labToDelete.id)
        self.assertEqual(0, len(LAB_SECTION.objects.filter(id=labToDelete.id)))
        self.assertEqual(0, len(A_LIST.objects.filter(labID=labToDelete.id)))

        labToDelete = LAB_SECTION.objects.create(name="Music Lab", courseID=5, labNumber=334,
                                                 time="4:00pm-6:00pm", location="MUS 125")
        labToDelete.save()

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        A_LIST.objects.create(assistantID=self.ASSISTANT.id, labID=labToDelete.id).save()
        self.TERMINAL.deleteLab(labToDelete.id)
        self.assertEqual(0, len(LAB_SECTION.objects.filter(id=self.labToDelete.id)))
        self.assertEqual(0, len(A_LIST.objects.filter(labID=labToDelete.id)))

        labToDelete = LAB_SECTION.objects.create(name="Music Lab", courseID=5, labNumber=334,
                                                 time="4:00pm-6:00pm", location="MUS 125")
        labToDelete.save()

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        A_LIST.objects.create(assistantID=self.ASSISTANT.id, labID=labToDelete.id).save()
        self.TERMINAL.deleteLab(labToDelete.id)
        self.assertEqual(1, len(LAB_SECTION.objects.filter(id=labToDelete.id)))
        self.assertEqual(1, len(A_LIST.objects.filter(labID=labToDelete.id)))

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        A_LIST.objects.create(assistantID=self.ASSISTANT.id, labID=labToDelete.id).save()
        self.TERMINAL.deleteLab(labToDelete.id)
        self.assertEqual(1, len(LAB_SECTION.objects.filter(id=labToDelete.id)))
        self.assertEqual(1, len(A_LIST.objects.filter(labID=labToDelete.id)))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        A_LIST.objects.create(assistantID=self.ASSISTANT.id, labID=labToDelete.id).save()
        self.TERMINAL.deleteLab(labToDelete.id)
        self.assertEqual(0, len(LAB_SECTION.objects.filter(id=labToDelete.id)))
        self.assertEqual(0, len(A_LIST.objects.filter(labID=labToDelete.id)))

        labToDelete = LAB_SECTION.objects.create(name="Music Lab", courseID=5, labNumber=334,
                                                 time="4:00pm-6:00pm", location="MUS 125")
        labToDelete.save()

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        A_LIST.objects.create(assistantID=self.ASSISTANT.id, labID=labToDelete.id).save()
        self.TERMINAL.deleteLab(labToDelete.id)
        self.assertEqual(0, len(LAB_SECTION.objects.filter(id=self.labToDelete.id)))
        self.assertEqual(0, len(A_LIST.objects.filter(labID=labToDelete.id)))

        labToDelete = LAB_SECTION.objects.create(name="Music Lab", courseID=5, labNumber=334,
                                                 time="4:00pm-6:00pm", location="MUS 125")
        labToDelete.save()

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        A_LIST.objects.create(assistantID=self.ASSISTANT.id, labID=labToDelete.id).save()
        self.TERMINAL.deleteLab(labToDelete.id)
        self.assertEqual(0, len(LAB_SECTION.objects.filter(id=labToDelete.id)))
        self.assertEqual(0, len(A_LIST.objects.filter(labID=labToDelete.id)))

        labToDelete = LAB_SECTION.objects.create(name="Music Lab", courseID=5, labNumber=334,
                                                 time="4:00pm-6:00pm", location="MUS 125")
        labToDelete.save()

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        A_LIST.objects.create(assistantID=self.ASSISTANT.id, labID=labToDelete.id).save()
        self.TERMINAL.deleteLab(labToDelete.id)
        self.assertEqual(0, len(LAB_SECTION.objects.filter(id=self.labToDelete.id)))
        self.assertEqual(0, len(A_LIST.objects.filter(labID=labToDelete.id)))

        labToDelete = LAB_SECTION.objects.create(name="Music Lab", courseID=5, labNumber=334,
                                                 time="4:00pm-6:00pm", location="MUS 125")
        labToDelete.save()

    # Create Course Tests

    def testCreateCourse(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.createCourse("Intro Python", "999", "232", "9:00am-11:00am", "COM 236")
        self.assertEqual("Intro Python", COURSE.objects.get(courseNumber="999", classNumber="232").name)
        COURSE.objects.filter(COURSE.objects.get(courseNumber="999", classNumber="232")).delete()

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.TERMINAL.createCourse("Intro Python", "999", "232", "9:00am-11:00am", "COM 236")
        self.assertEqual("Intro Python", COURSE.objects.get(courseNumber="999", classNumber="232").name)
        COURSE.objects.filter(COURSE.objects.get(courseNumber="999", classNumber="232")).delete()

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.createCourse("Intro Python", "999", "232", "9:00am-11:00am", "COM 236")
        self.assertEqual(0, COURSE.objects.filter(courseNumber="999", classNumber="232"))

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.createCourse("Intro Python", "999", "232", "9:00am-11:00am", "COM 236")
        self.assertEqual(0, COURSE.objects.filter(courseNumber="999", classNumber="232"))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.createCourse("Intro Python", "999", "232", "9:00am-11:00am", "COM 236")
        self.assertEqual("Intro Python", COURSE.objects.get(courseNumber="999", classNumber="232").name)
        COURSE.objects.filter(COURSE.objects.get(courseNumber="999", classNumber="232")).delete()

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.createCourse("Intro Python", "999", "232", "9:00am-11:00am", "COM 236")
        self.assertEqual("Intro Python", COURSE.objects.get(courseNumber="999", classNumber="232").name)
        COURSE.objects.filter(COURSE.objects.get(courseNumber="999", classNumber="232")).delete()

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.createCourse("Intro Python", "999", "232", "9:00am-11:00am", "COM 236")
        self.assertEqual("Intro Python", COURSE.objects.get(courseNumber="999", classNumber="232").name)
        COURSE.objects.filter(COURSE.objects.get(courseNumber="999", classNumber="232")).delete()

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.createCourse("Intro Python", "999", "232", "9:00am-11:00am", "COM 236")
        self.assertEqual("Intro Python", COURSE.objects.get(courseNumber="999", classNumber="232").name)
        COURSE.objects.filter(COURSE.objects.get(courseNumber="999", classNumber="232")).delete()

    def testCreateCourseDuplicateClassNumberAndCourseNumber(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.createCourse("Intro Python", "342", "234", "9:00am-11:00am", "COM 236")
        self.assertEqual(0, len(COURSE.objects.filter(courseNumber="342", classNumber="234")))

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.TERMINAL.createCourse("Intro Python", "342", "234", "9:00am-11:00am", "COM 236")
        self.assertEqual(0, len(COURSE.objects.filter(courseNumber="342", classNumber="234")))

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.createCourse("Intro Python", "342", "234", "9:00am-11:00am", "COM 236")
        self.assertEqual(0, len(COURSE.objects.filter(courseNumber="342", classNumber="234")))

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.createCourse("Intro Python", "342", "234", "9:00am-11:00am", "COM 236")
        self.assertEqual(0, len(COURSE.objects.filter(courseNumber="342", classNumber="234")))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.createCourse("Intro Python", "342", "234", "9:00am-11:00am", "COM 236")
        self.assertEqual(0, len(COURSE.objects.filter(courseNumber="342", classNumber="234")))

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.createCourse("Intro Python", "342", "234", "9:00am-11:00am", "COM 236")
        self.assertEqual(0, len(COURSE.objects.filter(courseNumber="342", classNumber="234")))

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.createCourse("Intro Python", "342", "234", "9:00am-11:00am", "COM 236")
        self.assertEqual(0, len(COURSE.objects.filter(courseNumber="342", classNumber="234")))

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.createCourse("Intro Python", "342", "234", "9:00am-11:00am", "COM 236")
        self.assertEqual(0, len(COURSE.objects.filter(courseNumber="342", classNumber="234")))

    def testCreateCourseMissingInput(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.createCourse("", "342", "234", "9:00am-11:00am", "COM 236")
        self.assertEqual(0, len(COURSE.objects.filter(courseNumber="342", classNumber="234")))

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.TERMINAL.createCourse("Intro Python", "342", "234", "", "COM 236")
        self.assertEqual(0, len(COURSE.objects.filter(courseNumber="342", classNumber="234")))

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.createCourse("Intro Python", "342", "234", "9:00am-11:00am", "")
        self.assertEqual(0, len(COURSE.objects.filter(courseNumber="342", classNumber="234")))

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.createCourse("Intro Python", "342", "234", "9:00am-11:00am", "")
        self.assertEqual(0, len(COURSE.objects.filter(courseNumber="342", classNumber="234")))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.createCourse("Intro Python", "", "234", "9:00am-11:00am", "COM 236")
        self.assertEqual(0, len(COURSE.objects.filter(name="Intro Python", classNumber="234")))

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.createCourse("Intro Python", "342", "", "9:00am-11:00am", "COM 236")
        self.assertEqual(0, len(COURSE.objects.filter(courseNumber="342", name="Intro Python")))

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.createCourse("Intro Python", "342", "234", "9:00am-11:00am", "")
        self.assertEqual(0, len(COURSE.objects.filter(courseNumber="342", classNumber="234")))

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.createCourse("", "342", "234", "9:00am-11:00am", "COM 236")
        self.assertEqual(0, len(COURSE.objects.filter(courseNumber="342", classNumber="234")))

    # Edit Course Tests

    def testEditCourse(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.editCourse(self.PHYSICS.id, "", "999", "", "", "")
        self.assertEqual(self.PHYSICS.courseNumber, COURSE.objects.get(id=self.PHYSICS.id),
                         msg="Changing the course number is dangerous, must delete and make a new course")

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.editCourse(self.PHYSICS.id, "", "", "1234", "", "")
        self.assertEqual(self.PHYSICS.courseNumber, COURSE.objects.get(id=self.PHYSICS.id),
                         msg="Changing the class number is dangerous, must delete and make a new course")

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.TERMINAL.editCourse(self.PHYSICS.id, "", "999", "", "", "")
        self.assertEqual(self.PHYSICS.courseNumber, COURSE.objects.get(id=self.PHYSICS.id),
                         msg="Changing the course number is dangerous, must delete and make a new course")

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.TERMINAL.editCourse(self.PHYSICS.id, "", "", "1234", "", "")
        self.assertEqual(self.PHYSICS.courseNumber, COURSE.objects.get(id=self.PHYSICS.id),
                         msg="Changing the class number is dangerous, must delete and make a new course")

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.editCourse(self.PHYSICS.id, "", "999", "", "", "")
        self.assertEqual(self.PHYSICS.courseNumber, COURSE.objects.get(id=self.PHYSICS.id),
                         msg="Changing the course number is dangerous, must delete and make a new course")

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.editCourse(self.PHYSICS.id, "", "", "1234", "", "")
        self.assertEqual(self.PHYSICS.courseNumber, COURSE.objects.get(id=self.PHYSICS.id),
                         msg="Changing the class number is dangerous, must delete and make a new course")

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.editCourse(self.PHYSICS.id, "", "999", "", "", "")
        self.assertEqual(self.PHYSICS.courseNumber, COURSE.objects.get(id=self.PHYSICS.id),
                         msg="Changing the course number is dangerous, must delete and make a new course")

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.editCourse(self.PHYSICS.id, "", "", "1234", "", "")
        self.assertEqual(self.PHYSICS.courseNumber, COURSE.objects.get(id=self.PHYSICS.id),
                         msg="Changing the class number is dangerous, must delete and make a new course")

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.editCourse(self.PHYSICS.id, "", "999", "", "", "")
        self.assertEqual(self.PHYSICS.courseNumber, COURSE.objects.get(id=self.PHYSICS.id),
                         msg="Changing the course number is dangerous, must delete and make a new course")

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.editCourse(self.PHYSICS.id, "", "", "1234", "", "")
        self.assertEqual(self.PHYSICS.courseNumber, COURSE.objects.get(id=self.PHYSICS.id),
                         msg="Changing the class number is dangerous, must delete and make a new course")

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.editCourse(self.PHYSICS.id, "", "999", "", "", "")
        self.assertEqual(self.PHYSICS.courseNumber, COURSE.objects.get(id=self.PHYSICS.id),
                         msg="Changing the course number is dangerous, must delete and make a new course")

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.editCourse(self.PHYSICS.id, "", "", "1234", "", "")
        self.assertEqual(self.PHYSICS.courseNumber, COURSE.objects.get(id=self.PHYSICS.id),
                         msg="Changing the class number is dangerous, must delete and make a new course")

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.editCourse(self.PHYSICS.id, "", "999", "", "", "")
        self.assertEqual(self.PHYSICS.courseNumber, COURSE.objects.get(id=self.PHYSICS.id),
                         msg="Changing the course number is dangerous, must delete and make a new course")

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.editCourse(self.PHYSICS.id, "", "", "1234", "", "")
        self.assertEqual(self.PHYSICS.courseNumber, COURSE.objects.get(id=self.PHYSICS.id),
                         msg="Changing the class number is dangerous, must delete and make a new course")

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.editCourse(self.PHYSICS.id, "", "999", "", "", "")
        self.assertEqual(self.PHYSICS.courseNumber, COURSE.objects.get(id=self.PHYSICS.id),
                         msg="Changing the course number is dangerous, must delete and make a new course")

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.editCourse(self.PHYSICS.id, "", "", "1234", "", "")
        self.assertEqual(self.PHYSICS.courseNumber, COURSE.objects.get(id=self.PHYSICS.id),
                         msg="Changing the class number is dangerous, must delete and make a new course")

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.editCourse(self.PHYSICS.id, "Cool Course", "", "", "", "")
        self.assertEqual("Cool Course", COURSE.objects.get(id=self.PHYSICS.id).name)
        self.assertEqual(self.PHYSICS.courseNumber, COURSE.objects.get(self.PHYSICS.id).courseNumber)
        self.assertEqual(self.PHYSICS.classNumber, COURSE.objects.get(self.PHYSICS.id).classNumber)
        self.assertEqual(self.PHYSICS.time, COURSE.objects.get(self.PHYSICS.id).time)
        self.assertEqual(self.PHYSICS.location, COURSE.objects.get(self.PHYSICS.id).location)
        course = COURSE.objects.get(id=self.PHYSICS.id)
        course.name = self.PHYSICS.name
        course.save()

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.editCourse(self.PHYSICS.id, "", "", "", "", "DeForest")
        self.assertEqual("DeForest", COURSE.objects.get(id=self.PHYSICS.id).location)
        self.assertEqual(self.PHYSICS.courseNumber, COURSE.objects.get(self.PHYSICS.id).courseNumber)
        self.assertEqual(self.PHYSICS.classNumber, COURSE.objects.get(self.PHYSICS.id).classNumber)
        self.assertEqual(self.PHYSICS.time, COURSE.objects.get(self.PHYSICS.id).time)
        self.assertEqual(self.PHYSICS.name, COURSE.objects.get(self.PHYSICS.id).name)
        course = COURSE.objects.get(id=self.PHYSICS.id)
        course.location= self.PHYSICS.location
        course.save()

    # Delete Course Tests

    def testDeleteCourse(self):
        courseToDelete = COURSE.objects.create(name="Physics", courseNumber=342, classNumber=111,
                                               time="7:00am-8:30am", location="PHY 324").save()
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.deleteCourse(courseToDelete.id)
        self.assertEqual(0, len(COURSE.objects.filter(id=courseToDelete.id)))
        courseToDelete.save()

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.TERMINAL.deleteCourse(courseToDelete.id)
        self.assertEqual(0, len(COURSE.objects.filter(id=courseToDelete.id)))
        courseToDelete.save()

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.deleteCourse(courseToDelete.id)
        self.assertEqual(1, len(COURSE.objects.filter(id=courseToDelete.id)))

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.deleteCourse(courseToDelete.id)
        self.assertEqual(1, len(COURSE.objects.filter(id=courseToDelete.id)))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.deleteCourse(courseToDelete.id)
        self.assertEqual(0, len(COURSE.objects.filter(id=courseToDelete.id)))
        courseToDelete.save()

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.deleteCourse(courseToDelete.id)
        self.assertEqual(0, len(COURSE.objects.filter(id=courseToDelete.id)))
        courseToDelete.save()

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.deleteCourse(courseToDelete.id)
        self.assertEqual(0, len(COURSE.objects.filter(id=courseToDelete.id)))
        courseToDelete.save()

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.deleteCourse(courseToDelete.id)
        self.assertEqual(0, len(COURSE.objects.filter(id=courseToDelete.id)))
        courseToDelete.save()

    def testDeleteCourseWithDependencies(self):
        courseToDelete = COURSE.objects.create(name="Physics", courseNumber=342, classNumber=111,
                                               time="7:00am-8:30am", location="PHY 324").save()
        labToDelete = LAB_SECTION.objects.create(name="Physics Lab", courseID=courseToDelete.id, labNumber=1444,
                                                 time="4:00pm-6:00pm", location="PHY 345").save()

        I_LIST.objects.create(instructorID=self.INSTRUCTOR.id, courseID=courseToDelete.id).save()
        I_LIST.objects.create(instructorID=self.ASSISTANT.id, courseID=courseToDelete.id).save()
        A_LIST.objects.create(assistantID=self.ASSISTANT.id, labID=labToDelete.id).save()
        I_LIST.objects.create(instructorID=self.SUPER_INSTRUCTOR.id, courseID=courseToDelete.id).save()

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.deleteCourse(courseToDelete.id)
        self.assertEqual(0, len(COURSE.objects.filter(id=courseToDelete.id)))
        self.assertEqual(0, len(I_LIST.objects.filter(courseID=courseToDelete.id, instructorID=self.INSTRUCTOR.id)))
        self.assertEqual(0, len(I_LIST.objects.filter(courseID=courseToDelete.id, instructorID=self.ASSISTANT.id)))
        self.assertEqual(0, len(I_LIST.objects.filter(courseID=courseToDelete.id, instructorID=self.SUPER_ASSISTANT.id)))
        self.assertEqual(0, len(A_LIST.objects.filter(courseID=courseToDelete.id, instructorID=self.ASSISTANT.id)))

    def testDeleteCourseDoesNotExist(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.deleteCourse("900")

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.TERMINAL.deleteCourse("900")

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.deleteCourse("900")

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.deleteCourse("900")

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.deleteCourse("900")

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.deleteCourse("900")

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.deleteCourse("900")

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.deleteCourse("900")


    # Create Account Tests

    def testCreateAccount(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.createAccount([1], "aUsername", "aPassword", "email@email.com", "Craig", "Smith",
                                    "1112223333", "2223334444", "34")
        self.assertEqual(1, len(USER.objects.filter(username="aUsername", password="aPassword")))
        USER.objects.get(username="aUsername", password="aPassword").delete()

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.TERMINAL.createAccount([1], "aUsername", "aPassword", "email@email.com", "Craig", "Smith",
                                    "1112223333", "2223334444", "34")
        self.assertEqual(1, len(USER.objects.filter(username="aUsername", password="aPassword")))
        USER.objects.get(username="aUsername", password="aPassword").delete()

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.createAccount([1], "aUsername", "aPassword", "email@email.com", "Craig", "Smith",
                                    "1112223333", "2223334444", "34")
        self.assertEqual(0, len(USER.objects.filter(username="aUsername", password="aPassword")))

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.createAccount([1], "aUsername", "aPassword", "email@email.com", "Craig", "Smith",
                                    "1112223333", "2223334444", "34")
        self.assertEqual(0, len(USER.objects.filter(username="aUsername", password="aPassword")))

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.createAccount([1], "aUsername", "aPassword", "email@email.com", "Craig", "Smith",
                                    "1112223333", "2223334444", "34")
        self.assertEqual(1, len(USER.objects.filter(username="aUsername", password="aPassword")))
        USER.objects.get(username="aUsername", password="aPassword").delete()

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.createAccount([1], "aUsername", "aPassword", "email@email.com", "Craig", "Smith",
                                    "1112223333", "2223334444", "34")
        self.assertEqual(1, len(USER.objects.filter(username="aUsername", password="aPassword")))
        USER.objects.get(username="aUsername", password="aPassword").delete()

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.createAccount([1], "aUsername", "aPassword", "email@email.com", "Craig", "Smith",
                                    "1112223333", "2223334444", "34")
        self.assertEqual(1, len(USER.objects.filter(username="aUsername", password="aPassword")))
        USER.objects.get(username="aUsername", password="aPassword").delete()

    def testCreateAccountDuplicate(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.createAccount([1], self.INSTRUCTOR.username, "aPassword", "email@email.com", "Craig", "Smith",
                                    "1112223333", "2223334444", "34")
        self.assertEqual(1, len(USER.objects.filter(username=self.INSTRUCTOR.username,
                                                    password=self.INSTRUCTOR.password)))

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.TERMINAL.createAccount([1], self.INSTRUCTOR.username, "aPassword", "email@email.com", "Craig", "Smith",
                                    "1112223333", "2223334444", "34")
        self.assertEqual(1, len(USER.objects.filter(username=self.INSTRUCTOR.username,
                                                    password=self.INSTRUCTOR.password)))

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.createAccount([1], self.INSTRUCTOR.username, "aPassword", "email@email.com", "Craig", "Smith",
                                    "1112223333", "2223334444", "34")
        self.assertEqual(1, len(USER.objects.filter(username=self.INSTRUCTOR.username,
                                                    password=self.INSTRUCTOR.password)))

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.createAccount([1], self.INSTRUCTOR.username, "aPassword", "email@email.com", "Craig", "Smith",
                                    "1112223333", "2223334444", "34")
        self.assertEqual(1, len(USER.objects.filter(username=self.INSTRUCTOR.username,
                                                    password=self.INSTRUCTOR.password)))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.createAccount([1], self.INSTRUCTOR.username, "aPassword", "email@email.com", "Craig", "Smith",
                                    "1112223333", "2223334444", "34")
        self.assertEqual(1, len(USER.objects.filter(username=self.INSTRUCTOR.username,
                                                    password=self.INSTRUCTOR.password)))

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.createAccount([1], self.INSTRUCTOR.username, "aPassword", "email@email.com", "Craig", "Smith",
                                    "1112223333", "2223334444", "34")
        self.assertEqual(1, len(USER.objects.filter(username=self.INSTRUCTOR.username,
                                                    password=self.INSTRUCTOR.password)))

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.createAccount([1], self.INSTRUCTOR.username, "aPassword", "email@email.com", "Craig", "Smith",
                                    "1112223333", "2223334444", "34")
        self.assertEqual(1, len(USER.objects.filter(username=self.INSTRUCTOR.username,
                                                    password=self.INSTRUCTOR.password)))

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.createAccount([1], self.INSTRUCTOR.username, "aPassword", "email@email.com", "Craig", "Smith",
                                    "1112223333", "2223334444", "34")
        self.assertEqual(1, len(USER.objects.filter(username=self.INSTRUCTOR.username,
                                                    password=self.INSTRUCTOR.password)))

    def testCreateAccountMissingInput(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.createAccount([1], "", "aPassword", "email@email.com", "Craig", "Smith",
                                    "1112223333", "2223334444", "34")
        self.assertEqual(0, len(USER.objects.filter(email="email@email.com", password="aPassword")))

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.createAccount([1], "aUsername", "", "email@email.com", "Craig", "Smith",
                                    "1112223333", "2223334444", "34")
        self.assertEqual(0, len(USER.objects.filter(email="email@email.com", username="aUsername")))

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.TERMINAL.createAccount([1], "", "aPassword", "email@email.com", "Craig", "Smith",
                                    "1112223333", "2223334444", "34")
        self.assertEqual(0, len(USER.objects.filter(email="email@email.com", password="aPassword")))

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.TERMINAL.createAccount([1], "aUsername", "", "email@email.com", "Craig", "Smith",
                                    "1112223333", "2223334444", "34")
        self.assertEqual(0, len(USER.objects.filter(email="email@email.com", username="aUsername")))

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.createAccount([1], "", "aPassword", "email@email.com", "Craig", "Smith",
                                    "1112223333", "2223334444", "34")
        self.assertEqual(0, len(USER.objects.filter(email="email@email.com", password="aPassword")))

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.createAccount([1], "aUsername", "", "email@email.com", "Craig", "Smith",
                                    "1112223333", "2223334444", "34")
        self.assertEqual(0, len(USER.objects.filter(email="email@email.com", username="aUsername")))

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.createAccount([1], "", "aPassword", "email@email.com", "Craig", "Smith",
                                    "1112223333", "2223334444", "34")
        self.assertEqual(0, len(USER.objects.filter(email="email@email.com", password="aPassword")))

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.createAccount([1], "aUsername", "", "email@email.com", "Craig", "Smith",
                                    "1112223333", "2223334444", "34")
        self.assertEqual(0, len(USER.objects.filter(email="email@email.com", username="aUsername")))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.createAccount([1], "", "aPassword", "email@email.com", "Craig", "Smith",
                                    "1112223333", "2223334444", "34")
        self.assertEqual(0, len(USER.objects.filter(email="email@email.com", password="aPassword")))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.createAccount([1], "aUsername", "", "email@email.com", "Craig", "Smith",
                                    "1112223333", "2223334444", "34")
        self.assertEqual(0, len(USER.objects.filter(email="email@email.com", username="aUsername")))

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.createAccount([1], "", "aPassword", "email@email.com", "Craig", "Smith",
                                    "1112223333", "2223334444", "34")
        self.assertEqual(0, len(USER.objects.filter(email="email@email.com", password="aPassword")))

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.createAccount([1], "aUsername", "", "email@email.com", "Craig", "Smith",
                                    "1112223333", "2223334444", "34")
        self.assertEqual(0, len(USER.objects.filter(email="email@email.com", username="aUsername")))

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.createAccount([1], "", "aPassword", "email@email.com", "Craig", "Smith",
                                    "1112223333", "2223334444", "34")
        self.assertEqual(0, len(USER.objects.filter(email="email@email.com", password="aPassword")))

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.createAccount([1], "aUsername", "", "email@email.com", "Craig", "Smith",
                                    "1112223333", "2223334444", "34")
        self.assertEqual(0, len(USER.objects.filter(email="email@email.com", username="aUsername")))

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.createAccount([1], "", "aPassword", "email@email.com", "Craig", "Smith",
                                    "1112223333", "2223334444", "34")
        self.assertEqual(0, len(USER.objects.filter(email="email@email.com", password="aPassword")))

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.createAccount([1], "aUsername", "", "email@email.com", "Craig", "Smith",
                                    "1112223333", "2223334444", "34")
        self.assertEqual(0, len(USER.objects.filter(email="email@email.com", username="aUsername")))


    # Edit Account Testsa

    def testEditAccount(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.editAccount(self.ASSISTANT.id, [1], "", "newPassword", "", "", "",
                                  "", "", "")
        self.assertEqual(1, len(USER.objects.filter(username=self.ASSISTANT.username, password="newPassword")))
        self.assertEqual(self.ASSISTANT.email, USER.objects.get(id=self.ASSISTANT.id))
        account = USER.objects.get(id=self.ASSISTANT.id)
        account.password = self.ASSISTANT.password
        account.save()

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.TERMINAL.editAccount(self.ASSISTANT.id, [1], "", "newPassword", "", "", "",
                                  "", "", "")
        self.assertEqual(1, len(USER.objects.filter(username=self.ASSISTANT.username, password="newPassword")))
        self.assertEqual(self.ASSISTANT.email, USER.objects.get(id=self.ASSISTANT.id))
        account = USER.objects.get(id=self.ASSISTANT.id)
        account.password = self.ASSISTANT.password
        account.save()

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.editAccount(self.ASSISTANT.id, [1], "", "newPassword", "", "", "",
                                  "", "", "")
        self.assertEqual(0, len(USER.objects.filter(username=self.ASSISTANT.username, password="newPassword")))

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.editAccount(self.ASSISTANT.id, [1], "", "newPassword", "", "", "",
                                  "", "", "")
        self.assertEqual(0, len(USER.objects.filter(username=self.ASSISTANT.username, password="newPassword")))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.editAccount(self.ASSISTANT.id, [1], "", "newPassword", "", "", "",
                                  "", "", "")
        self.assertEqual(1, len(USER.objects.filter(username=self.ASSISTANT.username, password="newPassword")))
        self.assertEqual(self.ASSISTANT.email, USER.objects.get(id=self.ASSISTANT.id))
        account = USER.objects.get(id=self.ASSISTANT.id)
        account.password = self.ASSISTANT.password
        account.save()

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.editAccount(self.ASSISTANT.id, [1], "", "newPassword", "", "", "",
                                  "", "", "")
        self.assertEqual(1, len(USER.objects.filter(username=self.ASSISTANT.username, password="newPassword")))
        self.assertEqual(self.ASSISTANT.email, USER.objects.get(id=self.ASSISTANT.id))
        account = USER.objects.get(id=self.ASSISTANT.id)
        account.password = self.ASSISTANT.password
        account.save()

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.editAccount(self.ASSISTANT.id, [1], "", "newPassword", "", "", "",
                                  "", "", "")
        self.assertEqual(1, len(USER.objects.filter(username=self.ASSISTANT.username, password="newPassword")))
        self.assertEqual(self.ASSISTANT.email, USER.objects.get(id=self.ASSISTANT.id))
        account = USER.objects.get(id=self.ASSISTANT.id)
        account.password = self.ASSISTANT.password
        account.save()

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.editAccount(self.ASSISTANT.id, [1], "", "newPassword", "", "", "",
                                  "", "", "")
        self.assertEqual(1, len(USER.objects.filter(username=self.ASSISTANT.username, password="newPassword")))
        self.assertEqual(self.ASSISTANT.email, USER.objects.get(id=self.ASSISTANT.id))
        account = USER.objects.get(id=self.ASSISTANT.id)
        account.password = self.ASSISTANT.password
        account.save()

    def testEditAccountToProduceDuplicate(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.editAccount(self.ASSISTANT.id, [1], self.INSTRUCTOR.username, "", "", "", "",
                                  "", "", "")
        self.assertEqual(0, len(USER.objects.filter(username=self.ASSISTANT.username,
                                                    password=self.INSTRUCTOR.username)))

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.TERMINAL.editAccount(self.ASSISTANT.id, [1], self.INSTRUCTOR.username, "", "", "", "",
                                  "", "", "")
        self.assertEqual(0, len(USER.objects.filter(username=self.ASSISTANT.username,
                                                    password=self.INSTRUCTOR.username)))

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.editAccount(self.ASSISTANT.id, [1], self.INSTRUCTOR.username, "", "", "", "",
                                  "", "", "")
        self.assertEqual(0, len(USER.objects.filter(username=self.ASSISTANT.username,
                                                    password=self.INSTRUCTOR.username)))

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.editAccount(self.ASSISTANT.id, [1], self.INSTRUCTOR.username, "", "", "", "",
                                  "", "", "")
        self.assertEqual(0, len(USER.objects.filter(username=self.ASSISTANT.username,
                                                    password=self.INSTRUCTOR.username)))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.editAccount(self.ASSISTANT.id, [1], self.INSTRUCTOR.username, "", "", "", "",
                                  "", "", "")
        self.assertEqual(0, len(USER.objects.filter(username=self.ASSISTANT.username,
                                                    password=self.INSTRUCTOR.username)))

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.editAccount(self.ASSISTANT.id, [1], self.INSTRUCTOR.username, "", "", "", "",
                                  "", "", "")
        self.assertEqual(0, len(USER.objects.filter(username=self.ASSISTANT.username,
                                                    password=self.INSTRUCTOR.username)))

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.editAccount(self.ASSISTANT.id, [1], self.INSTRUCTOR.username, "", "", "", "",
                                  "", "", "")
        self.assertEqual(0, len(USER.objects.filter(username=self.ASSISTANT.username,
                                                    password=self.INSTRUCTOR.username)))

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.editAccount(self.ASSISTANT.id, [1], self.INSTRUCTOR.username, "", "", "", "",
                                  "", "", "")
        self.assertEqual(0, len(USER.objects.filter(username=self.ASSISTANT.username,
                                                    password=self.INSTRUCTOR.username)))

    # Delete Account Tests

    def testDeleteAccount(self):
        userToDelete = USER.objects.create(permission=[1,3], username="aUsername", password="aPassword",
                                           email="email@email.com", firstName="James", lastName="Franco",
                                           contactPhone="3453334444", officePhone="3325554444",
                                           extension="2312").save()
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.deleteAccount(userid=userToDelete.id)
        self.assertEqual(0, USER.objects.filter(id=userToDelete.id))

        userToDelete.save()
        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.TERMINAL.deleteAccount(userid=userToDelete.id)
        self.assertEqual(0, USER.objects.filter(id=userToDelete.id))

        userToDelete.save()
        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.deleteAccount(userid=userToDelete.id)
        self.assertEqual(1, USER.objects.filter(id=userToDelete.id))

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.deleteAccount(userid=userToDelete.id)
        self.assertEqual(1, USER.objects.filter(id=userToDelete.id))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.deleteAccount(userid=userToDelete.id)
        self.assertEqual(0, USER.objects.filter(id=userToDelete.id))

        userToDelete.save()
        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.deleteAccount(userid=userToDelete.id)
        self.assertEqual(0, USER.objects.filter(id=userToDelete.id))

        userToDelete.save()
        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.deleteAccount(userid=userToDelete.id)
        self.assertEqual(0, USER.objects.filter(id=userToDelete.id))

        userToDelete.save()
        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.deleteAccount(userid=userToDelete.id)
        self.assertEqual(0, USER.objects.filter(id=userToDelete.id))

    def testDeleteAccountWithDependencies(self):
        userToDelete = USER.objects.create(permission=[1, 3], username="aUsername", password="aPassword",
                                           email="email@email.com", firstName="James", lastName="Franco",
                                           contactPhone="3453334444", officePhone="3325554444",
                                           extension="2312").save()

        otherUserToDelete = USER.objects.create(permission=[1, 4], username="bUsername", password="bPassword",
                                           email="email@email.com", firstName="will", lastName="fred",
                                           contactPhone="3453334444", officePhone="3325554444",
                                           extension="2312").save()

        I_LIST.objects.create(instructorID=userToDelete.id, courseID=self.PHYSICS.id).save()
        I_LIST.objects.create(instructorID=otherUserToDelete.id, courseID=self.PHYSICS.id).save()
        A_LIST.objects.create(assistantID=otherUserToDelete.id, labID=self.LAB_PHYSICS.id).save()

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)

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








