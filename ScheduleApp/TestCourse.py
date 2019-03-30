from django.test import TestCase

from ScheduleApp import Course


class TestCourse(TestCase):


    def testSomething(self):
        self.assertEqual(2, 2)

    def testDBID(self):
        c = Course()
        c.__setDataBaseID__(4080)
        self.assertEqual(c.__getDataBaseID__(), 4080)
    def test_get_class_number(self):
        c = Course()
        c.classNumber = 235
        self.assertEqual((235,c.getClassNumber))
    def test_set_class_number(self):
        c = Course()
        c.setClassNumber(55)
        self.assertEqual(55, c.classNumber)
    def test_get_time(self):
        c = Course()
        c.time = "14:20"
        self.assertEqual("14:20",c.get_time)
    def test_set_time(self):
        c = Course()
        c.set_time(15:00)
        self.assertEqual("15:00",c.time)
    def test_get_databaseID(self):
        c = Course()
        c.databaseID = 2134
        self.assertEqual(2134, c.getDataBaseID())
    def test_set_databaseID(self):
        c = Course()
        c.setDataBaseID(666)
        self.assertEqual(666,c.databaseID)
    def test_set_location(self):
        c = Course()
        c.set_location("EMS 156")
        self.assertEqual("EMS 156", c.location)
    def test_get_location(self):
        c = Course()
        c.location= "EMS 180"
        self.assertEqual("EMS 180", c.get_location)
    def test_add_lab(self):
        c = Course()
        c.add_lab()
        self.assertEqual(1, c.labList.count)
    def test_name_getter(self):
        c = Course()
        c.name = "Phy 209"
        self.assertEqual("Phy 209", c.get_name())
    def test_set_name(self):
        c = Course()
        c.setName("Phy 210")
        self.assertEqual("Phy 210", c.name)
    def  test_set_courseNumber(self):
        c = Course()
        c.set_courseNumber(111)
        self.assertEqual(111, c.courseNumber)
    def test_get_courseNumber(self):
        c = Course()
        c.courseNumber= 123
        self.assertEqual(123, c.get_courseNumber())






if __name__ == '__main__':
    unittest.main()
