from django.test import TestCase

from ScheduleApp import Course


class TestCourse(TestCase):


    def testSomething(self):
        self.assertEqual(2, 2)

    def testDBID(self):
        c = Course.Course(0, 'Intro to Software Enginerring', 361, 1, 0, 'EMSE150')
        c.setDataBaseID(4080)
        self.assertEqual(c.getDataBaseID(), 4080)
    def test_get_class_number(self):
        c = Course.Course(0, 'Intro to Software Enginerring', 361, 1, 0, 'EMSE150')
        c.classNumber = 235
        self.assertEqual(235, c.getClassNumber())
    def test_set_class_number(self):
        c = Course.Course(0, 'Intro to Software Enginerring', 361, 1, 0, 'EMSE150')
        c.setClassNumber(55)
        self.assertEqual(55, c.classNumber)
    def test_get_time(self):
        c = Course.Course(0, 'Intro to Software Enginerring', 361, 1, 0, 'EMSE150')
        c.time = "14:20"
        self.assertEqual("14:20", c.getTime())
    def test_set_time(self):
        c = Course.Course(0, 'Intro to Software Enginerring', 361, 1, 0, 'EMSE150')
        c.setTime("15:00")
        self.assertEqual("15:00",c.time)
    def test_get_databaseID(self):
        c = Course.Course(0, 'Intro to Software Enginerring', 361, 1, 0, 'EMSE150')
        c.databaseID = 2134
        self.assertEqual(2134, c.getDataBaseID())
    def test_set_databaseID(self):
        c = Course.Course(0, 'Intro to Software Enginerring', 361, 1, 0, 'EMSE150')
        c.setDataBaseID(666)
        self.assertEqual(666,c.databaseID)
    def test_set_location(self):
        c = Course.Course(0, 'Intro to Software Enginerring', 361, 1, 0, 'EMSE150')
        c.setLocation("EMS 156")
        self.assertEqual("EMS 156", c.location)
    def test_get_location(self):
        c = Course.Course(0, 'Intro to Software Enginerring', 361, 1, 0, 'EMSE150')
        c.location = "EMS 180"
        self.assertEqual("EMS 180", c.getLocation())
    def test_add_lab(self):
        c = Course.Course(0, 'Intro to Software Enginerring', 361, 1, 0, 'EMSE150')
        c.labList.append("")
        self.assertEqual(1, c.labList.count(""))
    def test_name_getter(self):
        c = Course.Course(0, 'Intro to Software Enginerring', 361, 1, 0, 'EMSE150')
        c.name = "Phy 209"
        self.assertEqual("Phy 209", c.getName())
    def test_set_name(self):
        c = Course.Course(0, 'Intro to Software Enginerring', 361, 1, 0, 'EMSE150')
        c.setName("Phy 210")
        self.assertEqual("Phy 210", c.name)
    def  test_set_courseNumber(self):
        c = Course.Course(0, 'Intro to Software Enginerring', 361, 1, 0, 'EMSE150')
        c.setCourseNumber(111)
        self.assertEqual(111, c.courseNumber)
    def test_get_courseNumber(self):
        c = Course.Course(0, 'Intro to Software Enginerring', 361, 1, 0, 'EMSE150')
        c.courseNumber= 123
        self.assertEqual(123, c.getCourseNumber())






if __name__ == '__main__':
    django.test.main()
