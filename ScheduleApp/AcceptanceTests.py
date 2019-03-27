from django.test import TestCase
from ScheduleApp import Commands, User, Course
from myApp.models import LAB_SECTION, COURSE, A_LIST, USER, I_LIST


class AcceptanceTests(TestCase):
    def setUp(self):
        LAB_SECTION.objects.create(databaseID = 1, name = "Physics", courseNumber =500, classNumber = 270, time= "9-10am", location = "Physics 270")
        USER.objects.create(permission = [2], username = "IPO", password = "pret212", databaseID = 69, email = "IPO@DEZN.com", firstName = "Bo", lastName = "fa", contactPhone = "2625874132", officePhone = "2625478669", extension = "148")
        COURSE.objects.create(databaseID = 645, name = "DEATHSCI", courseNumber = 500, classNumber = 204, labList = [804,803,802], time = "8-9am", location = "EMS 203")
        A_LIST.objects.create(courseID= 68, assistantID= 67)
        I_LIST.objects.create(courseID= 56, instructorID= 75)

    def test_things(self):
        self.assertEquals(Commands.CreateAccount("1, AKelly, password, Null, Null, Andrew, Kelly, 262-262-2626,"
                                                 " 414-414-4141, 5698"), "Account successfully created.")
        user = User
        user.permission = 1
        user2 = User
        user2.databaseID = 45
        self.assertEquals(Commands.DeleteAccount(user.permission, user2.databaseID), user2.username + "'s account has "
                                                                                                    "been deleted.")
        user3 = User
        self.assertEquals(Commands.EditAccount(user.permission, user3), "Account has been edited.")
        self.assertEquals(Commands.CreatCourse("CourseName, CourseNumber", "Course created."))
        self.assertEquals(Commands.Email("This is the email"), "Email sent.")
        self.assertEquals(Commands.AccessData("table name"), "data") #ALLL THE DAtA
        course1 = Course
        course1.courseNumber = 401
        self.assertEquals(Commands.AssignInstructorToCourse("401, AKelly"), "Instructor successfully added to course.")
        self.assertEquals(Commands.AssignAssistantToCourse("user, course1"), "TA successfully added to course.")
        self.assertEquals(Commands.ViewCourseAssignments(user), "Some Table")
        self.assertEquals(Commands.ViewAssistantAssignments(user), "Some Table")

    def test_create_course(self):
