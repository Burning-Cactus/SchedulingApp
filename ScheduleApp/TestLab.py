
from django.test import TestCase

from ScheduleApp import Lab
#

class LabTests(TestCase):


	#Getters and Setters
	#####Getters
	def testGetLabID(self):
		lab = Lab.Lab(1,"Intro to Software Engineering",361,1,"10:00-12:00","EMSE110",1)
		lab.labID = 2
		self.assertEqual(lab.labID, 2)
	def testGetName(self):
		lab = Lab.Lab(1, "Intro to Software Engineering", 361, 1, "10:00-12:00", "EMSE110", 1)
		lab.name = "Test"
		self.assertEqual(lab.getName(), "Test")
	def testGetLabNumber(self):
		lab = Lab.Lab(1, "Intro to Software Engineering", 361, 1, "10:00-12:00", "EMSE110", 1)
		lab.labNumber = 3
		self.assertEqual(lab.getLabNr(), 3)
	def testGetCourseID(self):
		lab = Lab.Lab(1, "Intro to Software Engineering", 361, 1, "10:00-12:00", "EMSE110", 1)
		lab.courseID = 3600
		self.assertEqual(lab.getCourseID(), 3600)
	def testGetTime(self):
		lab = Lab.Lab(1, "Intro to Software Engineering", 361, 1, "10:00-12:00", "EMSE110", 1)
		lab.time = "4-5pm"
		self.assertEqual(lab.getTime(), "4-5pm")
	def testGetLocation(self):
		lab = Lab.Lab(1, "Intro to Software Engineering", 361, 1, "10:00-12:00", "EMSE110", 1)
		lab.location = "EMSE110"
		self.assertEqual(lab.getLocation(), "EMSE110")
	def testGettaID(self):
		lab = Lab.Lab(1, "Intro to Software Engineering", 361, 1, "10:00-12:00", "EMSE110", 1)
		lab.classNumber = 2
		self.assertEqual(lab.getClassNr(), 2)
	#####Setters
	def testSetLabID(self):
		lab = Lab.Lab(1, "Intro to Software Engineering", 361, 1, "10:00-12:00", "EMSE110", 1)
		lab.setLabID(2)
		self.assertEqual(lab.labID, 2)
	def testSetName(self):
		lab = Lab.Lab(1, "Intro to Software Engineering", 361, 1, "10:00-12:00", "EMSE110", 1)
		lab.setName("Errorsss")
		self.assertEqual(lab.getName(), "Errorsss")
	def testSetLabNumber(self):
		lab = Lab.Lab(1, "Intro to Software Engineering", 361, 1, "10:00-12:00", "EMSE110", 1)
		lab.setLabNr(3)
		self.assertEqual(lab.labNumber, 3)
	def testSetCourseID(self):
		lab = Lab.Lab(1, "Intro to Software Engineering", 361, 1, "10:00-12:00", "EMSE110", 1)
		lab.setCourseID(3)
		self.assertEqual(lab.getCourseID(), 3)
	def testSetTime(self):
		lab = Lab.Lab(1, "Intro to Software Engineering", 361, 1, "10:00-12:00", "EMSE110", 1)
		lab.setTime("Forenoon")
		self.assertEqual(lab.getTime(), "Forenoon")
	def testSetLocation(self):
		lab = Lab.Lab(1, "Intro to Software Engineering", 361, 1, "10:00-12:00", "EMSE110", 1)
		lab.setLocation("Flipways")
		self.assertEqual(lab.getLocation(), "Flipways")
	def testSettaID(self):
		lab = Lab.Lab(1, "Intro to Software Engineering", 361, 1, "10:00-12:00", "EMSE110", 1)
		lab.setClassNr(3)
		self.assertEqual(lab.classNumber, 3)

if __name__ == '__main__':
	unittest.main()