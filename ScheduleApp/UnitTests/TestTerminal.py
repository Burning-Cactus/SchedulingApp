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
        COURSE.objects.create(name="Physics", courseNumber="342", classNumber="234",
                              time="7:00am-8:30am", location="PHY 324").save()
        COURSE.objects.create(name="Calculus", courseNumber="231", classNumber="432",
                              time="7:00am-8:30am", location="MATH 324").save()
        COURSE.objects.create(name="English", courseNumber="553", classNumber="342",
                              time="7:00am-8:30am", location="ENG 324").save()
        COURSE.objects.create(name="Art", courseNumber="456, classNumber=755",
                              time="7:00am-8:30am", location="ART 324").save()
        COURSE.objects.create(name="Music", courseNumber="675", classNumber="678",
                              time="7:00am-8:30am", location="MUS 324").save()

        # Populate LAB_SECTION Table
        LAB_SECTION.objects.create(name="Physics Lab", courseID="1", labNumber="765",
                                   time="4:00pm-6:00pm", location="PHY 345").save()
        LAB_SECTION.objects.create(name="Physics Lab", courseID="1", labNumber="743",
                                   time="4:00pm-6:00pm", location="PHY 342").save()
        LAB_SECTION.objects.create(name="Physics Lab", courseID="1", labNumber="967",
                                   time="4:00pm-6:00pm", location="PHY 457").save()
        LAB_SECTION.objects.create(name="Calculus Lab", courseID="2", labNumber="261",
                                   time="4:00pm-6:00pm", location="MATH 234").save()
        LAB_SECTION.objects.create(name="Calculus Lab", courseID="2", labNumber="643",
                                   time="4:00pm-6:00pm", location="MATH 345").save()
        LAB_SECTION.objects.create(name="Calculus Lab", courseID="2", labNumber="567",
                                   time="4:00pm-6:00pm", location="MATH 645").save()
        LAB_SECTION.objects.create(name="Art Lab", courseID="4", labNumber="453",
                                   time="4:00pm-6:00pm", location="ART 367").save()
        LAB_SECTION.objects.create(name="Art Lab", courseID="4", labNumber="473",
                                   time="4:00pm-6:00pm", location="ART 234").save()
        LAB_SECTION.objects.create(name="Music Lab", courseID="5", labNumber="956",
                                   time="4:00pm-6:00pm", location="MUS 345").save()
        LAB_SECTION.objects.create(name="Music Lab", courseID="5", labNumber="964",
                                   time="4:00pm-6:00pm", location="MUS 125").save()

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
        self.assertEqual(("Invalid username or password",False), self.TERMINAL.login("bad", "data"))
        self.assertEqual(("Invalid username or password",False), self.TERMINAL.login("bad", ""))
        self.assertEqual(("Invalid username or password",False), self.TERMINAL.login("", "data"))
        self.assertEqual(("Invalid username or password",False), self.TERMINAL.login("", ""))
        self.assertEqual(("Invalid username or password",False), self.TERMINAL.login("Wilton", "data"))

        # Partially Valid
        self.assertEqual(("Invalid username or password",False), self.TERMINAL.login("Wilton", ""))
        self.assertEqual(("Invalid username or password",False), self.TERMINAL.login("", "slick"))

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
        self.assertEqual((None,False), self.TERMINAL.createLab("Calculus Lab", "2", self.LAB_CALCULUS.labNumber, "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.assertEqual((None,False),
                         self.TERMINAL.createLab("Calculus Lab", "2", self.LAB_CALCULUS.labNumber, "4:00pm-6:00pm",
                                                 "MATH 231"))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.assertEqual((None,False),
                         self.TERMINAL.createLab("Calculus Lab", "2", self.LAB_CALCULUS.labNumber, "4:00pm-6:00pm",
                                                 "MATH 231"))

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.assertEqual((None,False),
                         self.TERMINAL.createLab("Calculus Lab", "2", self.LAB_CALCULUS.labNumber, "4:00pm-6:00pm",
                                                 "MATH 231"))

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.assertEqual((None,False),
                         self.TERMINAL.createLab("Calculus Lab", "2", self.LAB_CALCULUS.labNumber, "4:00pm-6:00pm",
                                                 "MATH 231"))

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.assertEqual((None,False),
                         self.TERMINAL.createLab("Calculus Lab", "2", self.LAB_CALCULUS.labNumber, "4:00pm-6:00pm",
                                                 "MATH 231"))

    def testCreateLabCourseDoesNotExist(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.assertEqual((None,False),
                         self.TERMINAL.createLab("Calculus Lab", "500", "100", "4:00pm-6:00pm",
                                                 "MATH 231"))

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.assertEqual((None,False),
                         self.TERMINAL.createLab("Calculus Lab", "500", "100", "4:00pm-6:00pm",
                                                 "MATH 231"))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.assertEqual((None,False),
                         self.TERMINAL.createLab("Calculus Lab", "500", "100", "4:00pm-6:00pm",
                                                 "MATH 231"))

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.assertEqual((None,False),
                         self.TERMINAL.createLab("Calculus Lab", "500", "100", "4:00pm-6:00pm",
                                                 "MATH 231"))

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.assertEqual((None,False),
                         self.TERMINAL.createLab("Calculus Lab", "500", "100", "4:00pm-6:00pm",
                                                 "MATH 231"))

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.assertEqual((None,False),
                         self.TERMINAL.createLab("Calculus Lab", "500", "100", "4:00pm-6:00pm",
                                                 "MATH 231"))

    def testCreateLabCourseIsNONE(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("Calculus Lab", None, "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("Calculus Lab", None, "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("Calculus Lab", None, "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("Calculus Lab", None, "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("Calculus Lab", None, "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("Calculus Lab", None, "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

    def testCreateLabMissingInput(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("", "2", "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("", "2", "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("", "2", "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("", "2", "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("", "2", "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("", "2", "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("Calculus Lab", "", "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("Calculus Lab", "", "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("Calculus Lab", "", "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("Calculus Lab", "", "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("Calculus Lab", "", "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("Calculus Lab", "", "100", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("Calculus Lab", "2", "", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("Calculus Lab", "2", "", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("Calculus Lab", "2", "", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("Calculus Lab", "2", "", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("Calculus Lab", "2", "", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("Calculus Lab", "2", "", "4:00pm-6:00pm",
                                                       "MATH 231"))

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("Calculus Lab", "2", "100", "",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("Calculus Lab", "2", "100", "",
                                                       "MATH 231"))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("Calculus Lab", "2", "100", "",
                                                       "MATH 231"))

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("Calculus Lab", "2", "100", "",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("Calculus Lab", "2", "100", "",
                                                       "MATH 231"))

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("Calculus Lab", "2", "100", "",
                                                       "MATH 231"))

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("Calculus Lab", "2", "100", "4:00pm-6:00pm",
                                                       ""))

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("Calculus Lab", "2", "100", "4:00pm-6:00pm",
                                                       ""))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("Calculus Lab", "2", "100", "4:00pm-6:00pm",
                                                       ""))

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("Calculus Lab", "2", "100", "4:00pm-6:00pm",
                                                       ""))

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("Calculus Lab", "2", "100", "4:00pm-6:00pm",
                                                       ""))

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.assertEqual((None,False), self.TERMINAL.createLab("Calculus Lab", "2", "100", "4:00pm-6:00pm",
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
        self.assertEqual(self.LAB_CALCULUS.location, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location)

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, self.LAB_CALCULUS.name, self.LAB_CALCULUS.courseID,
                              self.LAB_CALCULUS.labNumber, "", "MATH 900")
        self.assertEqual(self.LAB_CALCULUS.location, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location)

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
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, "Another Name", "", "", "", "")
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
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, "Another Name", "", "", "", "")
        self.assertEqual("Another Name", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).name)
        self.assertEqual(self.LAB_CALCULUS.courseID, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).courseID)
        self.assertEqual(self.LAB_CALCULUS.labNumber, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).labNumber)
        self.assertEqual(self.LAB_CALCULUS.time, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).time)
        self.assertEqual(self.LAB_CALCULUS.location, LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).location)
        # reset location value to what it was before edit
        lab = LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id)
        lab.name = self.LAB_CALCULUS.name
        lab.save()

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, "Another Name", "", "", "", "")
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
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, "Another Name", "", "", "", "")
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
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, "Another Name", "", "", "", "")
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
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, "Another Name", "", "", "", "")
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
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, "", "1", "", "", "")
        self.assertEqual("2", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).courseID)
        self.assertEqual(1, len(A_LIST.objects.filter(assistantID=self.ASSISTANT.id)))
        A_LIST.objects.get(assistantID=self.ASSISTANT.id).delete()

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        A_LIST.objects.create(assistantID=self.ASSISTANT.id, labID=self.LAB_CALCULUS.id).save()
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, "", "1", "", "", "")
        self.assertEqual("2", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).courseID)
        self.assertEqual(1, len(A_LIST.objects.filter(assistantID=self.ASSISTANT.id)))
        A_LIST.objects.get(assistantID=self.ASSISTANT.id).delete()

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        A_LIST.objects.create(assistantID=self.ASSISTANT.id, labID=self.LAB_CALCULUS.id).save()
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, "", "1", "", "", "")
        self.assertEqual("2", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).courseID)
        self.assertEqual(1, len(A_LIST.objects.filter(assistantID=self.ASSISTANT.id)))
        A_LIST.objects.get(assistantID=self.ASSISTANT.id).delete()

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        A_LIST.objects.create(assistantID=self.ASSISTANT.id, labID=self.LAB_CALCULUS.id).save()
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, "", "1", "", "", "")
        self.assertEqual("2", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).courseID)
        self.assertEqual(1, len(A_LIST.objects.filter(assistantID=self.ASSISTANT.id)))
        A_LIST.objects.get(assistantID=self.ASSISTANT.id).delete()

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        A_LIST.objects.create(assistantID=self.ASSISTANT.id, labID=self.LAB_CALCULUS.id).save()
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, "", "1", "", "", "")
        self.assertEqual("2", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).courseID)
        self.assertEqual(1, len(A_LIST.objects.filter(assistantID=self.ASSISTANT.id)))
        A_LIST.objects.get(assistantID=self.ASSISTANT.id).delete()

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        A_LIST.objects.create(assistantID=self.ASSISTANT.id, labID=self.LAB_CALCULUS.id).save()
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, "", "1", "", "", "")
        self.assertEqual("2", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).courseID)
        self.assertEqual(1, len(A_LIST.objects.filter(assistantID=self.ASSISTANT.id)))
        A_LIST.objects.get(assistantID=self.ASSISTANT.id).delete()

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        A_LIST.objects.create(assistantID=self.ASSISTANT.id, labID=self.LAB_CALCULUS.id).save()
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, "", "1", "", "", "")
        self.assertEqual("2", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).courseID)
        self.assertEqual(1, len(A_LIST.objects.filter(assistantID=self.ASSISTANT.id)))
        A_LIST.objects.get(assistantID=self.ASSISTANT.id).delete()

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        A_LIST.objects.create(assistantID=self.ASSISTANT.id, labID=self.LAB_CALCULUS.id).save()
        self.TERMINAL.editLab(self.LAB_CALCULUS.id, "", "1", "", "", "")
        self.assertEqual("2", LAB_SECTION.objects.get(id=self.LAB_CALCULUS.id).courseID)
        self.assertEqual(1, len(A_LIST.objects.filter(assistantID=self.ASSISTANT.id)))
        A_LIST.objects.get(assistantID=self.ASSISTANT.id).delete()

    # Delete Lab Tests

    def testDeleteLab(self):
        lab = LAB_SECTION.objects.create(name="Music Lab", courseID="5", labNumber="344", time="4:00pm-6:00pm",
                                         location="MUS 125")
        lab.save()
        labToDelete = LAB_SECTION.objects.get(courseID="5", labNumber="344")

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        A_LIST.objects.create(assistantID=self.ASSISTANT.id, labID=labToDelete.id).save()
        self.TERMINAL.deleteLab(labToDelete.id)
        self.assertEqual(0, len(LAB_SECTION.objects.filter(id=labToDelete.id)))
        self.assertEqual(0, len(A_LIST.objects.filter(labID=labToDelete.id)))

        lab.save()
        labToDelete = LAB_SECTION.objects.get(courseID="5", labNumber="344")
        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        A_LIST.objects.create(assistantID=self.ASSISTANT.id, labID=labToDelete.id).save()
        self.TERMINAL.deleteLab(labToDelete.id)
        self.assertEqual(0, len(LAB_SECTION.objects.filter(id=labToDelete.id)))
        self.assertEqual(0, len(A_LIST.objects.filter(labID=labToDelete.id)))

        lab.save()
        labToDelete = LAB_SECTION.objects.get(courseID="5", labNumber="344")
        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        A_LIST.objects.create(assistantID=self.ASSISTANT.id, labID=labToDelete.id).save()
        self.TERMINAL.deleteLab(labToDelete.id)
        self.assertEqual(1, len(LAB_SECTION.objects.filter(id=labToDelete.id)))
        self.assertEqual(1, len(A_LIST.objects.filter(labID=labToDelete.id)))

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.deleteLab(labToDelete.id)
        self.assertEqual(1, len(LAB_SECTION.objects.filter(id=labToDelete.id)))
        self.assertEqual(1, len(A_LIST.objects.filter(labID=labToDelete.id)))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        A_LIST.objects.create(assistantID=self.ASSISTANT.id, labID=labToDelete.id).save()
        self.TERMINAL.deleteLab(labToDelete.id)
        self.assertEqual(0, len(LAB_SECTION.objects.filter(id=labToDelete.id)))
        self.assertEqual(0, len(A_LIST.objects.filter(labID=labToDelete.id)))

        lab.save()
        labToDelete = LAB_SECTION.objects.get(courseID="5", labNumber="344")
        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        A_LIST.objects.create(assistantID=self.ASSISTANT.id, labID=labToDelete.id).save()
        self.TERMINAL.deleteLab(labToDelete.id)
        self.assertEqual(0, len(LAB_SECTION.objects.filter(id=labToDelete.id)))
        self.assertEqual(0, len(A_LIST.objects.filter(labID=labToDelete.id)))

        lab.save()
        labToDelete = LAB_SECTION.objects.get(courseID="5", labNumber="344")
        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        A_LIST.objects.create(assistantID=self.ASSISTANT.id, labID=labToDelete.id).save()
        self.TERMINAL.deleteLab(labToDelete.id)
        self.assertEqual(0, len(LAB_SECTION.objects.filter(id=labToDelete.id)))
        self.assertEqual(0, len(A_LIST.objects.filter(labID=labToDelete.id)))

        lab.save()
        labToDelete = LAB_SECTION.objects.get(courseID="5", labNumber="344")
        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        A_LIST.objects.create(assistantID=self.ASSISTANT.id, labID=labToDelete.id).save()
        self.TERMINAL.deleteLab(labToDelete.id)
        self.assertEqual(0, len(LAB_SECTION.objects.filter(id=labToDelete.id)))
        self.assertEqual(0, len(A_LIST.objects.filter(labID=labToDelete.id)))

    # Create Course Tests

    def testCreateCourse(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.createCourse("Intro Python", "999", "232", "9:00am-11:00am", "COM 236")
        self.assertEqual("Intro Python", COURSE.objects.get(courseNumber="999", classNumber="232").name)
        COURSE.objects.get(courseNumber="999", classNumber="232").delete()

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.TERMINAL.createCourse("Intro Python", "999", "232", "9:00am-11:00am", "COM 236")
        self.assertEqual("Intro Python", COURSE.objects.get(courseNumber="999", classNumber="232").name)
        COURSE.objects.get(courseNumber="999", classNumber="232").delete()

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.createCourse("Intro Python", "999", "232", "9:00am-11:00am", "COM 236")
        self.assertEqual(0, len(COURSE.objects.filter(courseNumber="999", classNumber="232")))

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.createCourse("Intro Python", "999", "232", "9:00am-11:00am", "COM 236")
        self.assertEqual(0, len(COURSE.objects.filter(courseNumber="999", classNumber="232")))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.createCourse("Intro Python", "999", "232", "9:00am-11:00am", "COM 236")
        self.assertEqual("Intro Python", COURSE.objects.get(courseNumber="999", classNumber="232").name)
        COURSE.objects.get(courseNumber="999", classNumber="232").delete()

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.createCourse("Intro Python", "999", "232", "9:00am-11:00am", "COM 236")
        self.assertEqual("Intro Python", COURSE.objects.get(courseNumber="999", classNumber="232").name)
        COURSE.objects.get(courseNumber="999", classNumber="232").delete()

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.createCourse("Intro Python", "999", "232", "9:00am-11:00am", "COM 236")
        self.assertEqual("Intro Python", COURSE.objects.get(courseNumber="999", classNumber="232").name)
        COURSE.objects.get(courseNumber="999", classNumber="232").delete()

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.createCourse("Intro Python", "999", "232", "9:00am-11:00am", "COM 236")
        self.assertEqual("Intro Python", COURSE.objects.get(courseNumber="999", classNumber="232").name)
        COURSE.objects.get(courseNumber="999", classNumber="232").delete()

    def testCreateCourseDuplicateClassNumberAndCourseNumber(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.createCourse("Intro Python", "342", "234", "9:00am-11:00am", "COM 236")
        self.assertEqual(1, len(COURSE.objects.filter(courseNumber="342", classNumber="234")))

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.TERMINAL.createCourse("Intro Python", "342", "234", "9:00am-11:00am", "COM 236")
        self.assertEqual(1, len(COURSE.objects.filter(courseNumber="342", classNumber="234")))

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.createCourse("Intro Python", "342", "234", "9:00am-11:00am", "COM 236")
        self.assertEqual(1, len(COURSE.objects.filter(courseNumber="342", classNumber="234")))

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.createCourse("Intro Python", "342", "234", "9:00am-11:00am", "COM 236")
        self.assertEqual(1, len(COURSE.objects.filter(courseNumber="342", classNumber="234")))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.createCourse("Intro Python", "342", "234", "9:00am-11:00am", "COM 236")
        self.assertEqual(1, len(COURSE.objects.filter(courseNumber="342", classNumber="234")))

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.createCourse("Intro Python", "342", "234", "9:00am-11:00am", "COM 236")
        self.assertEqual(1, len(COURSE.objects.filter(courseNumber="342", classNumber="234")))

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.createCourse("Intro Python", "342", "234", "9:00am-11:00am", "COM 236")
        self.assertEqual(1, len(COURSE.objects.filter(courseNumber="342", classNumber="234")))

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.createCourse("Intro Python", "342", "234", "9:00am-11:00am", "COM 236")
        self.assertEqual(1, len(COURSE.objects.filter(courseNumber="342", classNumber="234")))

    def testCreateCourseMissingInput(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.createCourse("", "111", "222", "9:00am-11:00am", "COM 236")
        self.assertEqual(0, len(COURSE.objects.filter(courseNumber="111", classNumber="222")))

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.TERMINAL.createCourse("Intro Python", "342", "234", "", "COM 236")
        self.assertEqual(0, len(COURSE.objects.filter(courseNumber="111", classNumber="222")))

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.createCourse("Intro Python", "342", "234", "9:00am-11:00am", "")
        self.assertEqual(0, len(COURSE.objects.filter(courseNumber="111", classNumber="222")))

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.createCourse("Intro Python", "342", "234", "9:00am-11:00am", "")
        self.assertEqual(0, len(COURSE.objects.filter(courseNumber="111", classNumber="222")))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.createCourse("Intro Python", "", "234", "9:00am-11:00am", "COM 236")
        self.assertEqual(0, len(COURSE.objects.filter(name="Intro Python", classNumber="222")))

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.createCourse("Intro Python", "342", "", "9:00am-11:00am", "COM 236")
        self.assertEqual(0, len(COURSE.objects.filter(courseNumber="111", name="Intro Python")))

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.createCourse("Intro Python", "342", "234", "9:00am-11:00am", "")
        self.assertEqual(0, len(COURSE.objects.filter(courseNumber="111", classNumber="222")))

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.createCourse("", "342", "234", "9:00am-11:00am", "COM 236")
        self.assertEqual(0, len(COURSE.objects.filter(courseNumber="111", classNumber="222")))

    # Edit Course Tests

    def testEditCourse(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.editCourse(self.PHYSICS.id, "", "999", "", "", "")
        self.assertEqual(self.PHYSICS.courseNumber, COURSE.objects.get(id=self.PHYSICS.id).courseNumber,
                         msg="Changing the course number is dangerous, must delete and make a new course")

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.TERMINAL.editCourse(self.PHYSICS.id, "", "999", "", "", "")
        self.assertEqual(self.PHYSICS.courseNumber, COURSE.objects.get(id=self.PHYSICS.id).courseNumber,
                         msg="Changing the course number is dangerous, must delete and make a new course")

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.editCourse(self.PHYSICS.id, "", "999", "", "", "")
        self.assertEqual(self.PHYSICS.courseNumber, COURSE.objects.get(id=self.PHYSICS.id).courseNumber,
                         msg="Changing the course number is dangerous, must delete and make a new course")

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.editCourse(self.PHYSICS.id, "", "999", "", "", "")
        self.assertEqual(self.PHYSICS.courseNumber, COURSE.objects.get(id=self.PHYSICS.id).courseNumber,
                         msg="Changing the course number is dangerous, must delete and make a new course")

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.editCourse(self.PHYSICS.id, "", "999", "", "", "")
        self.assertEqual(self.PHYSICS.courseNumber, COURSE.objects.get(id=self.PHYSICS.id).courseNumber,
                         msg="Changing the course number is dangerous, must delete and make a new course")

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.editCourse(self.PHYSICS.id, "", "999", "", "", "")
        self.assertEqual(self.PHYSICS.courseNumber, COURSE.objects.get(id=self.PHYSICS.id).courseNumber,
                         msg="Changing the course number is dangerous, must delete and make a new course")

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.editCourse(self.PHYSICS.id, "", "999", "", "", "")
        self.assertEqual(self.PHYSICS.courseNumber, COURSE.objects.get(id=self.PHYSICS.id).courseNumber,
                         msg="Changing the course number is dangerous, must delete and make a new course")

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.editCourse(self.PHYSICS.id, "", "999", "", "", "")
        self.assertEqual(self.PHYSICS.courseNumber, COURSE.objects.get(id=self.PHYSICS.id).courseNumber,
                         msg="Changing the course number is dangerous, must delete and make a new course")


        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.editCourse(self.PHYSICS.id, "Cool Course", "", "", "", "")
        self.assertEqual("Cool Course", COURSE.objects.get(id=self.PHYSICS.id).name)
        self.assertEqual(self.PHYSICS.courseNumber, COURSE.objects.get(id=self.PHYSICS.id).courseNumber)
        self.assertEqual(self.PHYSICS.classNumber, COURSE.objects.get(id=self.PHYSICS.id).classNumber)
        self.assertEqual(self.PHYSICS.time, COURSE.objects.get(id=self.PHYSICS.id).time)
        self.assertEqual(self.PHYSICS.location, COURSE.objects.get(id=self.PHYSICS.id).location)
        course = COURSE.objects.get(id=self.PHYSICS.id)
        course.name = self.PHYSICS.name
        course.save()

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.editCourse(self.PHYSICS.id, "", "", "", "", "DeForest")
        self.assertEqual("DeForest", COURSE.objects.get(id=self.PHYSICS.id).location)
        self.assertEqual(self.PHYSICS.courseNumber, COURSE.objects.get(id=self.PHYSICS.id).courseNumber)
        self.assertEqual(self.PHYSICS.classNumber, COURSE.objects.get(id=self.PHYSICS.id).classNumber)
        self.assertEqual(self.PHYSICS.time, COURSE.objects.get(id=self.PHYSICS.id).time)
        self.assertEqual(self.PHYSICS.name, COURSE.objects.get(id=self.PHYSICS.id).name)
        course = COURSE.objects.get(id=self.PHYSICS.id)
        course.location= self.PHYSICS.location
        course.save()

    # Delete Course Tests

    def testDeleteCourse(self):
        COURSE.objects.create(name="Physics", courseNumber="342", classNumber="111",
                                               time="7:00am-8:30am", location="PHY 324").save()
        courseToDelete = COURSE.objects.get(courseNumber="342", classNumber="111")

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
        COURSE.objects.create(name="Physics", courseNumber="342", classNumber="111", time="7:00am-8:30am",
                              location="PHY 324").save()
        courseToDelete = COURSE.objects.get(courseNumber="342", classNumber="111")

        LAB_SECTION.objects.create(name="Physics Lab", courseID=courseToDelete.id, labNumber="1444",
                                                 time="4:00pm-6:00pm", location="PHY 345").save()
        labToDelete = LAB_SECTION.objects.get(courseID=courseToDelete.id, labNumber="1444")

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
        self.assertEqual(0, len(A_LIST.objects.filter(labID=labToDelete.id, assistantID=self.ASSISTANT.id)))

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
        self.assertEqual(self.ASSISTANT.email, USER.objects.get(id=self.ASSISTANT.id).email)
        account = USER.objects.get(id=self.ASSISTANT.id)
        account.password = self.ASSISTANT.password
        account.permission = [4]
        account.save()

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.TERMINAL.editAccount(self.ASSISTANT.id, [1], "", "newPassword", "", "", "",
                                  "", "", "")
        self.assertEqual(1, len(USER.objects.filter(username=self.ASSISTANT.username, password="newPassword")))
        self.assertEqual(self.ASSISTANT.email, USER.objects.get(id=self.ASSISTANT.id).email)
        account = USER.objects.get(id=self.ASSISTANT.id)
        account.password = self.ASSISTANT.password
        account.permission = [4]
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
        self.assertEqual(self.ASSISTANT.email, USER.objects.get(id=self.ASSISTANT.id).email)
        account = USER.objects.get(id=self.ASSISTANT.id)
        account.password = self.ASSISTANT.password
        account.permission = [4]
        account.save()

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.editAccount(self.ASSISTANT.id, [1], "", "newPassword", "", "", "",
                                  "", "", "")
        self.assertEqual(1, len(USER.objects.filter(username=self.ASSISTANT.username, password="newPassword")))
        self.assertEqual(self.ASSISTANT.email, USER.objects.get(id=self.ASSISTANT.id).email)
        account = USER.objects.get(id=self.ASSISTANT.id)
        account.password = self.ASSISTANT.password
        account.permission = [4]
        account.save()

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.editAccount(self.ASSISTANT.id, [1], "", "newPassword", "", "", "",
                                  "", "", "")
        self.assertEqual(1, len(USER.objects.filter(username=self.ASSISTANT.username, password="newPassword")))
        self.assertEqual(self.ASSISTANT.email, USER.objects.get(id=self.ASSISTANT.id).email)
        account = USER.objects.get(id=self.ASSISTANT.id)
        account.password = self.ASSISTANT.password
        account.permission = [4]
        account.save()

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.editAccount(self.ASSISTANT.id, [1], "", "newPassword", "", "", "",
                                  "", "", "")
        self.assertEqual(1, len(USER.objects.filter(username=self.ASSISTANT.username, password="newPassword")))
        self.assertEqual(self.ASSISTANT.email, USER.objects.get(id=self.ASSISTANT.id).email)
        account = USER.objects.get(id=self.ASSISTANT.id)
        account.password = self.ASSISTANT.password
        account.permission = [4]
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
        USER.objects.create(permission=[1,3], username="aUsername", password="aPassword",
                                           email="email@email.com", firstName="James", lastName="Franco",
                                           contactPhone="3453334444", officePhone="3325554444",
                                           extension="2312").save()
        userToDelete = USER.objects.get(username="aUsername", password="aPassword")
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.deleteAccount(userid=userToDelete.id)
        self.assertEqual(0, len(USER.objects.filter(id=userToDelete.id)))

        userToDelete.save()
        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.TERMINAL.deleteAccount(userid=userToDelete.id)
        self.assertEqual(0, len(USER.objects.filter(id=userToDelete.id)))

        userToDelete.save()
        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.deleteAccount(userid=userToDelete.id)
        self.assertEqual(1, len(USER.objects.filter(id=userToDelete.id)))

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.deleteAccount(userid=userToDelete.id)
        self.assertEqual(1, len(USER.objects.filter(id=userToDelete.id)))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.deleteAccount(userid=userToDelete.id)
        self.assertEqual(0, len(USER.objects.filter(id=userToDelete.id)))

        userToDelete.save()
        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.deleteAccount(userid=userToDelete.id)
        self.assertEqual(0, len(USER.objects.filter(id=userToDelete.id)))

        userToDelete.save()
        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.deleteAccount(userid=userToDelete.id)
        self.assertEqual(0, len(USER.objects.filter(id=userToDelete.id)))

        userToDelete.save()
        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.deleteAccount(userid=userToDelete.id)
        self.assertEqual(0, len(USER.objects.filter(id=userToDelete.id)))

    def testDeleteAccountWithDependencies(self):
        USER.objects.create(permission=[1, 3], username="aUsername", password="aPassword",
                                           email="email@email.com", firstName="James", lastName="Franco",
                                           contactPhone="3453334444", officePhone="3325554444",
                                           extension="2312").save()
        userToDelete = USER.objects.get(username="aUsername", password="aPassword")

        USER.objects.create(permission=[1, 4], username="bUsername", password="bPassword",
                                                email="email@email.com", firstName="will", lastName="fred",
                                                contactPhone="3453334444", officePhone="3325554444",
                                                extension="2312").save()
        otherUserToDelete = USER.objects.get(username="bUsername", password="bPassword")

        I_LIST.objects.create(instructorID=userToDelete.id, courseID=self.PHYSICS.id).save()
        I_LIST.objects.create(instructorID=otherUserToDelete.id, courseID=self.PHYSICS.id).save()
        A_LIST.objects.create(assistantID=otherUserToDelete.id, labID=self.LAB_PHYSICS.id).save()

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.deleteAccount(userToDelete.id)
        self.TERMINAL.deleteAccount(otherUserToDelete.id)

        self.assertEqual(0, len(I_LIST.objects.filter(instructorID=userToDelete.id, courseID=self.PHYSICS.id)))
        self.assertEqual(0, len(I_LIST.objects.filter(instructorID=otherUserToDelete.id, courseID=self.PHYSICS.id)))
        self.assertEqual(0, len(A_LIST.objects.filter(assistantID=otherUserToDelete.id, labID=self.LAB_PHYSICS.id)))
        self.assertEqual(0, len(USER.objects.filter(id=userToDelete.id)))
        self.assertEqual(0, len(USER.objects.filter(id=otherUserToDelete.id)))

    # Email Tests

    def testEmail(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.email("subject", "message")

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.TERMINAL.email("subject", "message")

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.email("subject", "message")

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.email("subject", "message")

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.email("subject", "message")

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.email("subject", "message")

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.email("subject", "message")

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.email("subject", "message")

    # Accesss Data Tests

    def testAccessData(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.accessData()

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.TERMINAL.accessData()

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.accessData()

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.accessData()

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.accessData()

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.accessData()

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.accessData()

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.accessData()

    # Assign Instructor to Course Tests

    def testAssignInstructorPermissions(self):
        instructorToAssign = self.INSTRUCTOR

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.assignInstructorToCourse(self.ENGLISH.id, instructorToAssign.id)
        self.assertEqual(self.INSTRUCTOR.id, I_LIST.objects.get(courseID=self.ENGLISH.id,
                                                                instructorID=instructorToAssign.id).instructorID)
        I_LIST.objects.get(courseID=self.ENGLISH.id, instructorID=instructorToAssign.id).delete()

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.assignInstructorToCourse(self.ENGLISH.id, instructorToAssign.id)
        self.assertEqual(self.INSTRUCTOR.id, I_LIST.objects.get(courseID=self.ENGLISH.id,
                                                                instructorID=instructorToAssign.id).instructorID)
        I_LIST.objects.get(courseID=self.ENGLISH.id, instructorID=instructorToAssign.id).delete()

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.assignInstructorToCourse(self.ENGLISH.id, instructorToAssign.id)
        self.assertEqual(self.INSTRUCTOR.id, I_LIST.objects.get(courseID=self.ENGLISH.id,
                                                                instructorID=instructorToAssign.id).instructorID)
        I_LIST.objects.get(courseID=self.ENGLISH.id, instructorID=instructorToAssign.id).delete()

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.assignInstructorToCourse(self.ENGLISH.id, instructorToAssign.id)
        self.assertEqual(0, len(I_LIST.objects.filter(courseID=self.ENGLISH.id,
                                                      instructorID=instructorToAssign.id)))

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.assignInstructorToCourse(self.ENGLISH.id, instructorToAssign.id)
        self.assertEqual(0, len(I_LIST.objects.filter(courseID=self.ENGLISH.id,
                                                      instructorID=instructorToAssign.id)))

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.assignInstructorToCourse(self.ENGLISH.id, instructorToAssign.id)
        self.assertEqual(0, len(I_LIST.objects.filter(courseID=self.ENGLISH.id,
                                                      instructorID=instructorToAssign.id)))

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.assignInstructorToCourse(self.ENGLISH.id, instructorToAssign.id)
        self.assertEqual(0, len(I_LIST.objects.filter(courseID=self.ENGLISH.id,
                                                      instructorID=instructorToAssign.id)))

    def testAssignInstructorToCourse(self):
        instructorToAssign = self.INSTRUCTOR
        superInstructorToAssign = self.SUPER_INSTRUCTOR
        adminInstructorToAssign = self.ADMIN_INSTRUCTOR

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.assignInstructorToCourse(self.ENGLISH.id, instructorToAssign.id)
        self.TERMINAL.assignInstructorToCourse(self.ENGLISH.id, superInstructorToAssign.id)
        self.TERMINAL.assignInstructorToCourse(self.MUSIC.id, adminInstructorToAssign.id)
        self.TERMINAL.assignInstructorToCourse(self.PHYSICS.id, instructorToAssign.id)

        self.assertEqual(self.INSTRUCTOR.id, I_LIST.objects.get(courseID=self.ENGLISH.id,
                                                                instructorID=instructorToAssign.id).instructorID)

        self.assertEqual(self.SUPER_INSTRUCTOR.id, I_LIST.objects.get(courseID=self.ENGLISH.id,
                                                                      instructorID=superInstructorToAssign.id).instructorID)

        self.assertEqual(self.ADMIN_INSTRUCTOR.id, I_LIST.objects.get(courseID=self.MUSIC.id,
                                                                      instructorID=adminInstructorToAssign.id).instructorID)

        self.assertEqual(self.INSTRUCTOR.id, I_LIST.objects.get(courseID=self.PHYSICS.id,
                                                                instructorID=instructorToAssign.id).instructorID)

        I_LIST.objects.get(courseID=self.ENGLISH.id, instructorID=instructorToAssign.id).delete()
        I_LIST.objects.get(courseID=self.ENGLISH.id, instructorID=superInstructorToAssign.id).delete()
        I_LIST.objects.get(courseID=self.MUSIC.id, instructorID=adminInstructorToAssign.id).delete()
        I_LIST.objects.get(courseID=self.PHYSICS.id, instructorID=instructorToAssign.id).delete()

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.assignInstructorToCourse(self.ENGLISH.id, instructorToAssign.id)
        self.TERMINAL.assignInstructorToCourse(self.ENGLISH.id, superInstructorToAssign.id)
        self.TERMINAL.assignInstructorToCourse(self.MUSIC.id, adminInstructorToAssign.id)
        self.TERMINAL.assignInstructorToCourse(self.PHYSICS.id, instructorToAssign.id)

        self.assertEqual(self.INSTRUCTOR.id, I_LIST.objects.get(courseID=self.ENGLISH.id,
                                                                instructorID=instructorToAssign.id).instructorID)

        self.assertEqual(self.SUPER_INSTRUCTOR.id, I_LIST.objects.get(courseID=self.ENGLISH.id,
                                                                      instructorID=superInstructorToAssign.id).instructorID)

        self.assertEqual(self.ADMIN_INSTRUCTOR.id, I_LIST.objects.get(courseID=self.MUSIC.id,
                                                                      instructorID=adminInstructorToAssign.id).instructorID)

        self.assertEqual(self.INSTRUCTOR.id, I_LIST.objects.get(courseID=self.PHYSICS.id,
                                                                instructorID=instructorToAssign.id).instructorID)

        I_LIST.objects.get(courseID=self.ENGLISH.id, instructorID=instructorToAssign.id).delete()
        I_LIST.objects.get(courseID=self.ENGLISH.id, instructorID=superInstructorToAssign.id).delete()
        I_LIST.objects.get(courseID=self.MUSIC.id, instructorID=adminInstructorToAssign.id).delete()
        I_LIST.objects.get(courseID=self.PHYSICS.id, instructorID=instructorToAssign.id).delete()

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.assignInstructorToCourse(self.ENGLISH.id, instructorToAssign.id)
        self.TERMINAL.assignInstructorToCourse(self.ENGLISH.id, superInstructorToAssign.id)
        self.TERMINAL.assignInstructorToCourse(self.MUSIC.id, adminInstructorToAssign.id)
        self.TERMINAL.assignInstructorToCourse(self.PHYSICS.id, instructorToAssign.id)

        self.assertEqual(self.INSTRUCTOR.id, I_LIST.objects.get(courseID=self.ENGLISH.id,
                                                                instructorID=instructorToAssign.id).instructorID)

        self.assertEqual(self.SUPER_INSTRUCTOR.id, I_LIST.objects.get(courseID=self.ENGLISH.id,
                                                                      instructorID=superInstructorToAssign.id).instructorID)

        self.assertEqual(self.ADMIN_INSTRUCTOR.id, I_LIST.objects.get(courseID=self.MUSIC.id,
                                                                      instructorID=adminInstructorToAssign.id).instructorID)

        self.assertEqual(self.INSTRUCTOR.id, I_LIST.objects.get(courseID=self.PHYSICS.id,
                                                                instructorID=instructorToAssign.id).instructorID)

        I_LIST.objects.get(courseID=self.ENGLISH.id, instructorID=instructorToAssign.id).delete()
        I_LIST.objects.get(courseID=self.ENGLISH.id, instructorID=superInstructorToAssign.id).delete()
        I_LIST.objects.get(courseID=self.MUSIC.id, instructorID=adminInstructorToAssign.id).delete()
        I_LIST.objects.get(courseID=self.PHYSICS.id, instructorID=instructorToAssign.id).delete()

    def testAssignInstructorToCourseInstructorDoesNotExist(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.assignInstructorToCourse(self.ENGLISH.id, "3432")
        self.TERMINAL.assignInstructorToCourse(self.ENGLISH.id, "2346")
        self.TERMINAL.assignInstructorToCourse(self.MUSIC.id, "2343")
        self.TERMINAL.assignInstructorToCourse(self.PHYSICS.id, "9944")

        self.assertEqual(0, len(I_LIST.objects.filter(instructorID="3432")))
        self.assertEqual(0, len(I_LIST.objects.filter(instructorID="2346")))
        self.assertEqual(0, len(I_LIST.objects.filter(instructorID="2343")))
        self.assertEqual(0, len(I_LIST.objects.filter(instructorID="9944")))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.assignInstructorToCourse(self.ENGLISH.id, "3432")
        self.TERMINAL.assignInstructorToCourse(self.ENGLISH.id, "2346")
        self.TERMINAL.assignInstructorToCourse(self.MUSIC.id, "2343")
        self.TERMINAL.assignInstructorToCourse(self.PHYSICS.id, "9944")

        self.assertEqual(0, len(I_LIST.objects.filter(instructorID="3432")))
        self.assertEqual(0, len(I_LIST.objects.filter(instructorID="2346")))
        self.assertEqual(0, len(I_LIST.objects.filter(instructorID="2343")))
        self.assertEqual(0, len(I_LIST.objects.filter(instructorID="9944")))

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.assignInstructorToCourse(self.ENGLISH.id, "3432")
        self.TERMINAL.assignInstructorToCourse(self.ENGLISH.id, "2346")
        self.TERMINAL.assignInstructorToCourse(self.MUSIC.id, "2343")
        self.TERMINAL.assignInstructorToCourse(self.PHYSICS.id, "9944")

        self.assertEqual(0, len(I_LIST.objects.filter(instructorID="3432")))
        self.assertEqual(0, len(I_LIST.objects.filter(instructorID="2346")))
        self.assertEqual(0, len(I_LIST.objects.filter(instructorID="2343")))
        self.assertEqual(0, len(I_LIST.objects.filter(instructorID="9944")))

    def testAssignInstructorToCourseUserIsNotInstructor(self):
        supervisorToAssign = self.SUPERVISOR

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.assignInstructorToCourse(self.ENGLISH.id, supervisorToAssign.id)
        self.assertEqual(0, len(I_LIST.objects.filter(courseID=self.ENGLISH.id,
                                                      instructorID=supervisorToAssign.id)))

        adminToAssign = self.ADMINISTRATOR

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.assignInstructorToCourse(self.ENGLISH.id, adminToAssign.id)
        self.assertEqual(0, len(I_LIST.objects.filter(courseID=self.ENGLISH.id,
                                                      instructorID=adminToAssign.id)))

        superAssistantToAssign = self.SUPER_ASSISTANT

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.assignInstructorToCourse(self.ENGLISH.id, superAssistantToAssign.id)
        self.assertEqual(0, len(I_LIST.objects.filter(courseID=self.ENGLISH.id,
                                                      instructorID=superAssistantToAssign.id)))

        adminAssistantToAssign = self.ADMIN_ASSISTANT

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.assignInstructorToCourse(self.ENGLISH.id, adminAssistantToAssign.id)
        self.assertEqual(0, len(I_LIST.objects.filter(courseID=self.ENGLISH.id,
                                                      instructorID=adminAssistantToAssign.id)))

    def testAssignInstructorToCourseCourseDoesNotExist(self):
        instructorToAssign = self.INSTRUCTOR

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.assignInstructorToCourse("9000", instructorToAssign.id)
        self.assertEqual(0, len(I_LIST.objects.filter(courseID="9000", instructorID=instructorToAssign.id)))

    def testAssignInstructorToCourseInstructorAlreadyAssigned(self):
        instructorToAssign = self.INSTRUCTOR

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.assignInstructorToCourse(self.ENGLISH.id, instructorToAssign.id)
        self.assertEqual(1, len(I_LIST.objects.filter(courseID=self.ENGLISH.id, instructorID=instructorToAssign.id)))

        self.TERMINAL.assignInstructorToCourse(self.ENGLISH.id, instructorToAssign.id)
        self.assertEqual(1, len(I_LIST.objects.filter(courseID=self.ENGLISH.id, instructorID=instructorToAssign.id)))

        I_LIST.objects.get(courseID=self.ENGLISH.id, instructorID=instructorToAssign.id).delete()

    # Assign Assistant to Course Tests

    def testAssignAssistantPermissions(self):
        assistantToAssign = self.ASSISTANT

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.assignAssistantToCourse(self.ENGLISH.id, assistantToAssign.id)
        self.assertEqual(self.ASSISTANT.id, I_LIST.objects.get(courseID=self.ENGLISH.id,
                                                                instructorID=assistantToAssign.id).instructorID)
        I_LIST.objects.get(courseID=self.ENGLISH.id, instructorID=assistantToAssign.id).delete()

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.assignAssistantToCourse(self.ENGLISH.id, assistantToAssign.id)
        self.assertEqual(self.ASSISTANT.id, I_LIST.objects.get(courseID=self.ENGLISH.id,
                                                                instructorID=assistantToAssign.id).instructorID)
        I_LIST.objects.get(courseID=self.ENGLISH.id, instructorID=assistantToAssign.id).delete()

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.assignAssistantToCourse(self.ENGLISH.id, assistantToAssign.id)
        self.assertEqual(self.ASSISTANT.id, I_LIST.objects.get(courseID=self.ENGLISH.id,
                                                                instructorID=assistantToAssign.id).instructorID)
        I_LIST.objects.get(courseID=self.ENGLISH.id, instructorID=assistantToAssign.id).delete()

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.assignAssistantToCourse(self.ENGLISH.id, assistantToAssign.id)
        self.assertEqual(0, len(I_LIST.objects.filter(courseID=self.ENGLISH.id,
                                                      instructorID=assistantToAssign.id)))

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.assignAssistantToCourse(self.ENGLISH.id, assistantToAssign.id)
        self.assertEqual(0, len(I_LIST.objects.filter(courseID=self.ENGLISH.id,
                                                      instructorID=assistantToAssign.id)))

        self.TERMINAL.login(self.ADMIN_ASSISTANT.username, self.ADMIN_ASSISTANT.password)
        self.TERMINAL.assignAssistantToCourse(self.ENGLISH.id, assistantToAssign.id)
        self.assertEqual(0, len(I_LIST.objects.filter(courseID=self.ENGLISH.id,
                                                      instructorID=assistantToAssign.id)))

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.assignAssistantToCourse(self.ENGLISH.id, assistantToAssign.id)
        self.assertEqual(0, len(I_LIST.objects.filter(courseID=self.ENGLISH.id,
                                                      instructorID=assistantToAssign.id)))

    def testAssignAssistantToCourse(self):
        assistantToAssign = self.ASSISTANT
        superAssistantToAssign = self.SUPER_ASSISTANT
        adminAssistantToAssign = self.ADMIN_ASSISTANT

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.assignAssistantToCourse(self.ENGLISH.id, assistantToAssign.id)
        self.TERMINAL.assignAssistantToCourse(self.ENGLISH.id, superAssistantToAssign.id)
        self.TERMINAL.assignAssistantToCourse(self.MUSIC.id, adminAssistantToAssign.id)
        self.TERMINAL.assignAssistantToCourse(self.PHYSICS.id, assistantToAssign.id)

        self.assertEqual(self.ASSISTANT.id, I_LIST.objects.get(courseID=self.ENGLISH.id,
                                                               instructorID=assistantToAssign.id).instructorID)

        self.assertEqual(self.SUPER_ASSISTANT.id, I_LIST.objects.get(courseID=self.ENGLISH.id,
                                                                     instructorID=superAssistantToAssign.id).instructorID)

        self.assertEqual(self.ADMIN_ASSISTANT.id, I_LIST.objects.get(courseID=self.MUSIC.id,
                                                                     instructorID=adminAssistantToAssign.id).instructorID)

        self.assertEqual(self.ASSISTANT.id, I_LIST.objects.get(courseID=self.PHYSICS.id,
                                                               instructorID=assistantToAssign.id).instructorID)

        I_LIST.objects.get(courseID=self.ENGLISH.id, instructorID=assistantToAssign.id).delete()
        I_LIST.objects.get(courseID=self.ENGLISH.id, instructorID=superAssistantToAssign.id).delete()
        I_LIST.objects.get(courseID=self.MUSIC.id, instructorID=adminAssistantToAssign.id).delete()
        I_LIST.objects.get(courseID=self.PHYSICS.id, instructorID=assistantToAssign.id).delete()

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.assignAssistantToCourse(self.ENGLISH.id, assistantToAssign.id)
        self.TERMINAL.assignAssistantToCourse(self.ENGLISH.id, superAssistantToAssign.id)
        self.TERMINAL.assignAssistantToCourse(self.MUSIC.id, adminAssistantToAssign.id)
        self.TERMINAL.assignAssistantToCourse(self.PHYSICS.id, assistantToAssign.id)

        self.assertEqual(self.ASSISTANT.id, I_LIST.objects.get(courseID=self.ENGLISH.id,
                                                               instructorID=assistantToAssign.id).instructorID)

        self.assertEqual(self.SUPER_ASSISTANT.id, I_LIST.objects.get(courseID=self.ENGLISH.id,
                                                                     instructorID=superAssistantToAssign.id).instructorID)

        self.assertEqual(self.ADMIN_ASSISTANT.id, I_LIST.objects.get(courseID=self.MUSIC.id,
                                                                     instructorID=adminAssistantToAssign.id).instructorID)

        self.assertEqual(self.ASSISTANT.id, I_LIST.objects.get(courseID=self.PHYSICS.id,
                                                               instructorID=assistantToAssign.id).instructorID)

        I_LIST.objects.get(courseID=self.ENGLISH.id, instructorID=assistantToAssign.id).delete()
        I_LIST.objects.get(courseID=self.ENGLISH.id, instructorID=superAssistantToAssign.id).delete()
        I_LIST.objects.get(courseID=self.MUSIC.id, instructorID=adminAssistantToAssign.id).delete()
        I_LIST.objects.get(courseID=self.PHYSICS.id, instructorID=assistantToAssign.id).delete()

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.assignAssistantToCourse(self.ENGLISH.id, assistantToAssign.id)
        self.TERMINAL.assignAssistantToCourse(self.ENGLISH.id, superAssistantToAssign.id)
        self.TERMINAL.assignAssistantToCourse(self.MUSIC.id, adminAssistantToAssign.id)
        self.TERMINAL.assignAssistantToCourse(self.PHYSICS.id, assistantToAssign.id)

        self.assertEqual(self.ASSISTANT.id, I_LIST.objects.get(courseID=self.ENGLISH.id,
                                                               instructorID=assistantToAssign.id).instructorID)

        self.assertEqual(self.SUPER_ASSISTANT.id, I_LIST.objects.get(courseID=self.ENGLISH.id,
                                                                     instructorID=superAssistantToAssign.id).instructorID)

        self.assertEqual(self.ADMIN_ASSISTANT.id, I_LIST.objects.get(courseID=self.MUSIC.id,
                                                                     instructorID=adminAssistantToAssign.id).instructorID)

        self.assertEqual(self.ASSISTANT.id, I_LIST.objects.get(courseID=self.PHYSICS.id,
                                                               instructorID=assistantToAssign.id).instructorID)

        I_LIST.objects.get(courseID=self.ENGLISH.id, instructorID=assistantToAssign.id).delete()
        I_LIST.objects.get(courseID=self.ENGLISH.id, instructorID=superAssistantToAssign.id).delete()
        I_LIST.objects.get(courseID=self.MUSIC.id, instructorID=adminAssistantToAssign.id).delete()
        I_LIST.objects.get(courseID=self.PHYSICS.id, instructorID=assistantToAssign.id).delete()

    def testAssignAssistantToCourseAssistantDoesNotExist(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.assignAssistantToCourse(self.ENGLISH.id, "3432")
        self.TERMINAL.assignAssistantToCourse(self.ENGLISH.id, "2346")
        self.TERMINAL.assignAssistantToCourse(self.MUSIC.id, "2343")
        self.TERMINAL.assignAssistantToCourse(self.PHYSICS.id, "9944")

        self.assertEqual(0, len(I_LIST.objects.filter(instructorID="3432")))
        self.assertEqual(0, len(I_LIST.objects.filter(instructorID="2346")))
        self.assertEqual(0, len(I_LIST.objects.filter(instructorID="2343")))
        self.assertEqual(0, len(I_LIST.objects.filter(instructorID="9944")))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.assignAssistantToCourse(self.ENGLISH.id, "3432")
        self.TERMINAL.assignAssistantToCourse(self.ENGLISH.id, "2346")
        self.TERMINAL.assignAssistantToCourse(self.MUSIC.id, "2343")
        self.TERMINAL.assignAssistantToCourse(self.PHYSICS.id, "9944")

        self.assertEqual(0, len(I_LIST.objects.filter(instructorID="3432")))
        self.assertEqual(0, len(I_LIST.objects.filter(instructorID="2346")))
        self.assertEqual(0, len(I_LIST.objects.filter(instructorID="2343")))
        self.assertEqual(0, len(I_LIST.objects.filter(instructorID="9944")))

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.assignAssistantToCourse(self.ENGLISH.id, "3432")
        self.TERMINAL.assignAssistantToCourse(self.ENGLISH.id, "2346")
        self.TERMINAL.assignAssistantToCourse(self.MUSIC.id, "2343")
        self.TERMINAL.assignAssistantToCourse(self.PHYSICS.id, "9944")

        self.assertEqual(0, len(I_LIST.objects.filter(instructorID="3432")))
        self.assertEqual(0, len(I_LIST.objects.filter(instructorID="2346")))
        self.assertEqual(0, len(I_LIST.objects.filter(instructorID="2343")))
        self.assertEqual(0, len(I_LIST.objects.filter(instructorID="9944")))

    def testAssignAssistantToCourseUserIsNotAssistant(self):
        supervisorToAssign = self.SUPERVISOR

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.assignAssistantToCourse(self.ENGLISH.id, supervisorToAssign.id)
        self.assertEqual(0, len(I_LIST.objects.filter(courseID=self.ENGLISH.id,
                                                      instructorID=supervisorToAssign.id)))

        adminToAssign = self.ADMINISTRATOR

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.assignAssistantToCourse(self.ENGLISH.id, adminToAssign.id)
        self.assertEqual(0, len(I_LIST.objects.filter(courseID=self.ENGLISH.id,
                                                      instructorID=adminToAssign.id)))

        superInstructorToAssign = self.SUPER_INSTRUCTOR

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.assignAssistantToCourse(self.ENGLISH.id, superInstructorToAssign.id)
        self.assertEqual(0, len(I_LIST.objects.filter(courseID=self.ENGLISH.id,
                                                      instructorID=superInstructorToAssign.id)))

        adminInstructorToAssign = self.ADMIN_INSTRUCTOR

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.assignAssistantToCourse(self.ENGLISH.id, adminInstructorToAssign.id)
        self.assertEqual(0, len(I_LIST.objects.filter(courseID=self.ENGLISH.id,
                                                      instructorID=adminInstructorToAssign.id)))

    def testAssignAssistantToCourseCourseDoesNotExist(self):
        assistantToAssign = self.ASSISTANT

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.assignAssistantToCourse("9000", assistantToAssign.id)
        self.assertEqual(0, len(I_LIST.objects.filter(courseID="9000", instructorID=assistantToAssign.id)))

    def testAssignAssistantToCourseAssistantAlreadyAssigned(self):
        assistantToAssign = self.ASSISTANT

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.assignAssistantToCourse(self.ENGLISH.id, assistantToAssign.id)
        self.assertEqual(1, len(I_LIST.objects.filter(courseID=self.ENGLISH.id, instructorID=assistantToAssign.id)))

        self.TERMINAL.assignAssistantToCourse(self.ENGLISH.id, assistantToAssign.id)
        self.assertEqual(1, len(I_LIST.objects.filter(courseID=self.ENGLISH.id, instructorID=assistantToAssign.id)))

        I_LIST.objects.get(courseID=self.ENGLISH.id, instructorID=assistantToAssign.id).delete()

    # Assign Assistant to Lab Tests

    def testAssignAssistantToLabPermissions(self):
        assistantToAssign = self.ASSISTANT

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, assistantToAssign.id)
        self.assertEqual(self.ASSISTANT.id, A_LIST.objects.get(labID=self.LAB_PHYSICS.id,
                                                               assistantID=assistantToAssign.id).assistantID)
        A_LIST.objects.get(labID=self.LAB_PHYSICS.id, assistantID=assistantToAssign.id).delete()

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, assistantToAssign.id)
        self.assertEqual(self.ASSISTANT.id, A_LIST.objects.get(labID=self.LAB_PHYSICS.id,
                                                               assistantID=assistantToAssign.id).assistantID)
        A_LIST.objects.get(labID=self.LAB_PHYSICS.id, assistantID=assistantToAssign.id).delete()

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, assistantToAssign.id)
        self.assertEqual(self.ASSISTANT.id, A_LIST.objects.get(labID=self.LAB_PHYSICS.id,
                                                               assistantID=assistantToAssign.id).assistantID)
        A_LIST.objects.get(labID=self.LAB_PHYSICS.id, assistantID=assistantToAssign.id).delete()

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, assistantToAssign.id)
        self.assertEqual(self.ASSISTANT.id, A_LIST.objects.get(labID=self.LAB_PHYSICS.id,
                                                               assistantID=assistantToAssign.id).assistantID)
        A_LIST.objects.get(labID=self.LAB_PHYSICS.id, assistantID=assistantToAssign.id).delete()

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, assistantToAssign.id)
        self.assertEqual(self.ASSISTANT.id, A_LIST.objects.get(labID=self.LAB_PHYSICS.id,
                                                               assistantID=assistantToAssign.id).assistantID)
        A_LIST.objects.get(labID=self.LAB_PHYSICS.id, assistantID=assistantToAssign.id).delete()

        self.TERMINAL.login(self.ADMINISTRATOR.username, self.ADMINISTRATOR.password)
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, assistantToAssign.id)
        self.assertEqual(0, len(A_LIST.objects.filter(labID=self.LAB_PHYSICS.id, assistantID=assistantToAssign.id)))

        self.TERMINAL.login(self.ASSISTANT.username, self.ASSISTANT.password)
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, assistantToAssign.id)
        self.assertEqual(0, len(A_LIST.objects.filter(labID=self.LAB_PHYSICS.id, assistantID=assistantToAssign.id)))

    def testAssignAssistantToLab(self):
        assistantToAssign = self.ASSISTANT
        superAssistantToAssign = self.SUPER_ASSISTANT
        adminAssistantToAssign = self.ADMIN_ASSISTANT

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, assistantToAssign.id)
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, superAssistantToAssign.id)
        self.TERMINAL.assignAssistantToLab(self.LAB_ART.id, adminAssistantToAssign.id)
        self.TERMINAL.assignAssistantToLab(self.LAB_CALCULUS.id, assistantToAssign.id)

        self.assertEqual(self.ASSISTANT.id, A_LIST.objects.get(labID=self.LAB_PHYSICS.id,
                                                               assistantID=assistantToAssign.id).assistantID)

        self.assertEqual(self.SUPER_ASSISTANT.id, A_LIST.objects.get(labID=self.LAB_PHYSICS.id,
                                                                     assistantID=superAssistantToAssign.id).assistantID)

        self.assertEqual(self.ADMIN_ASSISTANT.id, A_LIST.objects.get(labID=self.LAB_ART.id,
                                                                     assistantID=adminAssistantToAssign.id).assistantID)

        self.assertEqual(self.ASSISTANT.id, A_LIST.objects.get(labID=self.LAB_CALCULUS.id,
                                                               assistantID=assistantToAssign.id).assistantID)

        A_LIST.objects.get(labID=self.LAB_PHYSICS.id, assistantID=assistantToAssign.id).delete()
        A_LIST.objects.get(labID=self.LAB_PHYSICS.id, assistantID=superAssistantToAssign.id).delete()
        A_LIST.objects.get(labID=self.LAB_ART.id, assistantID=adminAssistantToAssign.id).delete()
        A_LIST.objects.get(labID=self.LAB_CALCULUS.id, assistantID=assistantToAssign.id).delete()

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, assistantToAssign.id)
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, superAssistantToAssign.id)
        self.TERMINAL.assignAssistantToLab(self.LAB_ART.id, adminAssistantToAssign.id)
        self.TERMINAL.assignAssistantToLab(self.LAB_CALCULUS.id, assistantToAssign.id)

        self.assertEqual(self.ASSISTANT.id, A_LIST.objects.get(labID=self.LAB_PHYSICS.id,
                                                               assistantID=assistantToAssign.id).assistantID)

        self.assertEqual(self.SUPER_ASSISTANT.id, A_LIST.objects.get(labID=self.LAB_PHYSICS.id,
                                                                     assistantID=superAssistantToAssign.id).assistantID)

        self.assertEqual(self.ADMIN_ASSISTANT.id, A_LIST.objects.get(labID=self.LAB_ART.id,
                                                                     assistantID=adminAssistantToAssign.id).assistantID)

        self.assertEqual(self.ASSISTANT.id, A_LIST.objects.get(labID=self.LAB_CALCULUS.id,
                                                               assistantID=assistantToAssign.id).assistantID)

        A_LIST.objects.get(labID=self.LAB_PHYSICS.id, assistantID=assistantToAssign.id).delete()
        A_LIST.objects.get(labID=self.LAB_PHYSICS.id, assistantID=superAssistantToAssign.id).delete()
        A_LIST.objects.get(labID=self.LAB_ART.id, assistantID=adminAssistantToAssign.id).delete()
        A_LIST.objects.get(labID=self.LAB_CALCULUS.id, assistantID=assistantToAssign.id).delete()

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, assistantToAssign.id)
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, superAssistantToAssign.id)
        self.TERMINAL.assignAssistantToLab(self.LAB_ART.id, adminAssistantToAssign.id)
        self.TERMINAL.assignAssistantToLab(self.LAB_CALCULUS.id, assistantToAssign.id)

        self.assertEqual(self.ASSISTANT.id, A_LIST.objects.get(labID=self.LAB_PHYSICS.id,
                                                               assistantID=assistantToAssign.id).assistantID)

        self.assertEqual(self.SUPER_ASSISTANT.id, A_LIST.objects.get(labID=self.LAB_PHYSICS.id,
                                                                     assistantID=superAssistantToAssign.id).assistantID)

        self.assertEqual(self.ADMIN_ASSISTANT.id, A_LIST.objects.get(labID=self.LAB_ART.id,
                                                                     assistantID=adminAssistantToAssign.id).assistantID)

        self.assertEqual(self.ASSISTANT.id, A_LIST.objects.get(labID=self.LAB_CALCULUS.id,
                                                               assistantID=assistantToAssign.id).assistantID)

        A_LIST.objects.get(labID=self.LAB_PHYSICS.id, assistantID=assistantToAssign.id).delete()
        A_LIST.objects.get(labID=self.LAB_PHYSICS.id, assistantID=superAssistantToAssign.id).delete()
        A_LIST.objects.get(labID=self.LAB_ART.id, assistantID=adminAssistantToAssign.id).delete()
        A_LIST.objects.get(labID=self.LAB_CALCULUS.id, assistantID=assistantToAssign.id).delete()

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, assistantToAssign.id)
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, superAssistantToAssign.id)
        self.TERMINAL.assignAssistantToLab(self.LAB_ART.id, adminAssistantToAssign.id)
        self.TERMINAL.assignAssistantToLab(self.LAB_CALCULUS.id, assistantToAssign.id)

        self.assertEqual(self.ASSISTANT.id, A_LIST.objects.get(labID=self.LAB_PHYSICS.id,
                                                               assistantID=assistantToAssign.id).assistantID)

        self.assertEqual(self.SUPER_ASSISTANT.id, A_LIST.objects.get(labID=self.LAB_PHYSICS.id,
                                                                     assistantID=superAssistantToAssign.id).assistantID)

        self.assertEqual(self.ADMIN_ASSISTANT.id, A_LIST.objects.get(labID=self.LAB_ART.id,
                                                                     assistantID=adminAssistantToAssign.id).assistantID)

        self.assertEqual(self.ASSISTANT.id, A_LIST.objects.get(labID=self.LAB_CALCULUS.id,
                                                               assistantID=assistantToAssign.id).assistantID)

        A_LIST.objects.get(labID=self.LAB_PHYSICS.id, assistantID=assistantToAssign.id).delete()
        A_LIST.objects.get(labID=self.LAB_PHYSICS.id, assistantID=superAssistantToAssign.id).delete()
        A_LIST.objects.get(labID=self.LAB_ART.id, assistantID=adminAssistantToAssign.id).delete()
        A_LIST.objects.get(labID=self.LAB_CALCULUS.id, assistantID=assistantToAssign.id).delete()

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, assistantToAssign.id)
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, superAssistantToAssign.id)
        self.TERMINAL.assignAssistantToLab(self.LAB_ART.id, adminAssistantToAssign.id)
        self.TERMINAL.assignAssistantToLab(self.LAB_CALCULUS.id, assistantToAssign.id)

        self.assertEqual(self.ASSISTANT.id, A_LIST.objects.get(labID=self.LAB_PHYSICS.id,
                                                               assistantID=assistantToAssign.id).assistantID)

        self.assertEqual(self.SUPER_ASSISTANT.id, A_LIST.objects.get(labID=self.LAB_PHYSICS.id,
                                                                     assistantID=superAssistantToAssign.id).assistantID)

        self.assertEqual(self.ADMIN_ASSISTANT.id, A_LIST.objects.get(labID=self.LAB_ART.id,
                                                                     assistantID=adminAssistantToAssign.id).assistantID)

        self.assertEqual(self.ASSISTANT.id, A_LIST.objects.get(labID=self.LAB_CALCULUS.id,
                                                               assistantID=assistantToAssign.id).assistantID)

        A_LIST.objects.get(labID=self.LAB_PHYSICS.id, assistantID=assistantToAssign.id).delete()
        A_LIST.objects.get(labID=self.LAB_PHYSICS.id, assistantID=superAssistantToAssign.id).delete()
        A_LIST.objects.get(labID=self.LAB_ART.id, assistantID=adminAssistantToAssign.id).delete()
        A_LIST.objects.get(labID=self.LAB_CALCULUS.id, assistantID=assistantToAssign.id).delete()

    def testAssignAssistantToLabAssistantDoesNotExist(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.assignAssistantToLab(self.LAB_CALCULUS.id, "3432")
        self.TERMINAL.assignAssistantToLab(self.LAB_ART.id, "2346")
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, "2343")
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, "9944")

        self.assertEqual(0, len(A_LIST.objects.filter(assistantID="3432")))
        self.assertEqual(0, len(A_LIST.objects.filter(assistantID="2346")))
        self.assertEqual(0, len(A_LIST.objects.filter(assistantID="2343")))
        self.assertEqual(0, len(A_LIST.objects.filter(assistantID="9944")))

        self.TERMINAL.login(self.SUPER_ASSISTANT.username, self.SUPER_ASSISTANT.password)
        self.TERMINAL.assignAssistantToLab(self.LAB_CALCULUS.id, "3432")
        self.TERMINAL.assignAssistantToLab(self.LAB_ART.id, "2346")
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, "2343")
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, "9944")

        self.assertEqual(0, len(A_LIST.objects.filter(assistantID="3432")))
        self.assertEqual(0, len(A_LIST.objects.filter(assistantID="2346")))
        self.assertEqual(0, len(A_LIST.objects.filter(assistantID="2343")))
        self.assertEqual(0, len(A_LIST.objects.filter(assistantID="9944")))

        self.TERMINAL.login(self.SUPER_INSTRUCTOR.username, self.SUPER_INSTRUCTOR.password)
        self.TERMINAL.assignAssistantToLab(self.LAB_CALCULUS.id, "3432")
        self.TERMINAL.assignAssistantToLab(self.LAB_ART.id, "2346")
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, "2343")
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, "9944")

        self.assertEqual(0, len(A_LIST.objects.filter(assistantID="3432")))
        self.assertEqual(0, len(A_LIST.objects.filter(assistantID="2346")))
        self.assertEqual(0, len(A_LIST.objects.filter(assistantID="2343")))
        self.assertEqual(0, len(A_LIST.objects.filter(assistantID="9944")))

        self.TERMINAL.login(self.ADMIN_INSTRUCTOR.username, self.ADMIN_INSTRUCTOR.password)
        self.TERMINAL.assignAssistantToLab(self.LAB_CALCULUS.id, "3432")
        self.TERMINAL.assignAssistantToLab(self.LAB_ART.id, "2346")
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, "2343")
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, "9944")

        self.assertEqual(0, len(A_LIST.objects.filter(assistantID="3432")))
        self.assertEqual(0, len(A_LIST.objects.filter(assistantID="2346")))
        self.assertEqual(0, len(A_LIST.objects.filter(assistantID="2343")))
        self.assertEqual(0, len(A_LIST.objects.filter(assistantID="9944")))

        self.TERMINAL.login(self.INSTRUCTOR.username, self.INSTRUCTOR.password)
        self.TERMINAL.assignAssistantToLab(self.LAB_CALCULUS.id, "3432")
        self.TERMINAL.assignAssistantToLab(self.LAB_ART.id, "2346")
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, "2343")
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, "9944")

        self.assertEqual(0, len(A_LIST.objects.filter(assistantID="3432")))
        self.assertEqual(0, len(A_LIST.objects.filter(assistantID="2346")))
        self.assertEqual(0, len(A_LIST.objects.filter(assistantID="2343")))
        self.assertEqual(0, len(A_LIST.objects.filter(assistantID="9944")))

    def testAssignAssistantToLabUserIsNotAssistant(self):
        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, self.SUPERVISOR.id)
        self.assertEqual(0, len(A_LIST.objects.filter(labID=self.ENGLISH.id,
                                                      assistantID=self.SUPERVISOR.id)))

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, self.INSTRUCTOR.id)
        self.assertEqual(0, len(A_LIST.objects.filter(labID=self.LAB_PHYSICS.id,
                                                      assistantID=self.INSTRUCTOR.id)))

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, self.SUPER_INSTRUCTOR.id)
        self.assertEqual(0, len(A_LIST.objects.filter(labID=self.LAB_PHYSICS.id,
                                                      assistantID=self.SUPER_INSTRUCTOR.id)))

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, self.ADMIN_INSTRUCTOR.id)
        self.assertEqual(0, len(A_LIST.objects.filter(labID=self.LAB_PHYSICS.id,
                                                      assistantID=self.ADMIN_INSTRUCTOR.id)))

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, self.SUPER_INSTRUCTOR.id)
        self.assertEqual(0, len(A_LIST.objects.filter(labID=self.ADMINISTRATOR.id,
                                                      assistantID=self.ADMINISTRATOR.id)))

    def testAssignAssistantToLabLabDoesNotExist(self):
        assistantToAssign = self.ASSISTANT

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.assignAssistantToLab("9000", assistantToAssign.id)
        self.assertEqual(0, len(A_LIST.objects.filter(labID="9000", assistantID=assistantToAssign.id)))

    def testAssignAssistantToLabAssistantAlreadyAssigned(self):
        assistantToAssign = self.ASSISTANT

        self.TERMINAL.login(self.SUPERVISOR.username, self.SUPERVISOR.password)
        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, assistantToAssign.id)
        self.assertEqual(1, len(A_LIST.objects.filter(labID=self.LAB_PHYSICS.id, assistantID=assistantToAssign.id)))

        self.TERMINAL.assignAssistantToLab(self.LAB_PHYSICS.id, assistantToAssign.id)
        self.assertEqual(1, len(A_LIST.objects.filter(labID=self.LAB_PHYSICS.id, assistantID=assistantToAssign.id)))

        A_LIST.objects.get(labID=self.LAB_PHYSICS.id, assistantID=assistantToAssign.id).delete()

    # View Course Assignments Tests

    def testViewCourseAssignments(self):
        pass

    # View Assistant Assignemnts Tests

    def testViewAssisntantAssignments(self):
        pass

    # View Contact Info Tests

    def testViewContactInfo(self):
        pass
