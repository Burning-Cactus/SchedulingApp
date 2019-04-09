from . import Lab

#Lab (data structure: class) Unit Tests
#Tests:
	#CreateLab()
	#CreateLab(int labID/databaseID, string name, int labNumber (section), int courseID, time, location)
	#toString()
	#fromString()
	#updateDatabase()
	#and all the getters and setters
		#databaseID, name, labname, classname, time, location

import unittest

class LabTests(unittest.TestCase):
#LabTests: We're doing science now
	labDefault = Lab()
	#"a" might not be able to be ran fast enough to match the above. 
	#a = int(round(time.time() * 1000))
	
	lab = Lab("If you see this, tell a programmer", 1, 3600, "4-5pm", "A bad location to program")
	
	labDefault.settaID(1)
	lab.settaID(2)

	#CreateLab()
	#Going to default to:
		#labID: int(round(time.time() * 1000))
		#name: "Lab"
		#labNumber (section): 1
		#courseID: 101
		#time: "9-10am"
		#location: "Location"
		#(May not be needed) taID: 0 (a foreign key, so it is set from another table)
    def testCreateLabDefault(self):
        self.assertEqual(lab.labID, a)
		self.assertEqual(lab.name, "Lab")
		self.assertEqual(lab.labNumber, 1)
		self.assertEqual(lab.courseID, 101)
		self.assertEqual(lab.time, "9-10am")
		self.assertEqual(lab.location, "Location")
		#taID is set by another class
		#self.assertEqual(labDefault.taID, 0)

	#CreateLab(int labID/databaseID, string name, int labNumber (section), int courseID, time, location)
	def testLabCreate(self):
        self.assertEqual(labDefault.labID, a)
		self.assertEqual(labDefault.name, "If you see this, tell a programmer")
		self.assertEqual(labDefault.labNumber, 1)
		self.assertEqual(labDefault.courseID, 3600)
		self.assertEqual(labDefault.time, "4-5pm")
		self.assertEqual(labDefault.location, "A bad location to program")
		#taID is set by another class
		#self.assertEqual(labDefault.taID, 0)

	#toString()
		#Will output "labID,name,labNumber,courseID,time,location,taID" 
		#Probably don't want this to be comma separated if locations can have commas. 
		#Might cause some problems if not parsed well.
	def testToString(self):
		self.assertEqual(labDefault.toString(),labDefault.labID+","+labDefault.name+","+labDefault.labNumber+","+labDefault.courseID+","+labDefault.time+","+labDefault.location+","+labDefault.taID)
		self.assertEqual(lab.toString(),lab.labID+","+lab.name+","+lab.labNumber+","+lab.courseID+","+lab.time+","+lab.location+","+lab.taID)

	#fromString()
		#Accepts in the format: "labID,name,labNumber,courseID,time,location,taID" 
	def testFromString(self):
		andy = Create(1, "Andy's Test", 24, 7, "all day, erreday", "El Helado")
		cloneOfAndy = andy
		andy.fromString(lab.toString())
		self.assertEqual(andy.labID, cloneOfAndy.labID)
		self.assertEqual(andy.name, cloneOfAndy.name)
		self.assertEqual(andy.labNumber, cloneOfAndy.labNumber)
		self.assertEqual(andy.courseID, cloneOfAndy.courseID)
		self.assertEqual(andy.time, cloneOfAndy.time)
		self.assertEqual(andy.location, cloneOfAndy.location)
		self.assertEqual(andy.taID, cloneOfAndy.taID)
	
	#updateDatabase()
	def testUpdateDatabase(self):
		
	
	#Getters and Setters
	#####Getters
	def testGetLabID(self):
        self.assertEqual(labDefault.getLabID(), a)
		self.assertEqual(lab.getLabID(), a)
	def testGetName(self):
        self.assertEqual(labDefault.getName(), "Lab")
		self.assertEqual(lab.getName(), "If you see this, tell a programmer")
	def testGetLabNumber(self):
        self.assertEqual(labDefault.getLabNumber(), 1)
		self.assertEqual(lab.getLabNumber(), 1)
	def testGetCourseID(self):
        self.assertEqual(labDefault.getCourseID(), 101)
		self.assertEqual(lab.getCourseID(), 3600)
	def testGetTime(self):
        self.assertEqual(labDefault.getTime(), "9-10am")
		self.assertEqual(lab.getTime(), "4-5pm")
	def testGetLocation(self):
        self.assertEqual(labDefault.getLocation(), "Location")
		self.assertEqual(lab.getLocation(), "A bad location to program")
	def testGettaID(self):
		self.assertEqual(labDefault.gettaID(), 1)
		self.assertEqual(lab.gettaID(), 2)
	#####Setters
	def testSetLabID(self):
		labDefault.setLabID(a+1)
		lab.setLabID(a+2)
        self.assertEqual(labDefault.getLabID(), a+1)
		self.assertEqual(lab.getLabID(), a+2)
	def testSetName(self):
		labDefault.setName("Lab 2")
		lab.setName("Errorsss")
        self.assertEqual(labDefault.getName(), "Lab 2")
		self.assertEqual(lab.getName(), "Errorsss")
	def testSetLabNumber(self):
		labDefault.setLabID(2)
		lab.setLabID(3)
        self.assertEqual(labDefault.getLabID(), 2)
		self.assertEqual(lab.getLabID(), 3)
	def testSetCourseID(self):
		labDefault.setCourseID(2)
		lab.setCourseID(3)
        self.assertEqual(labDefault.getCourseID(), 2)
		self.assertEqual(lab.getCourseID(), 3)
	def testSetTime(self):
		labDefault.setTime("Midnight")
		lab.setTime("Forenoon")
        self.assertEqual(labDefault.getTime(), "Midnight")
		self.assertEqual(lab.getTime(), "Forenoon")
	def testSetLocation(self):
		labDefault.setLocation("Up")
		lab.setLocation("Flipways")
        self.assertEqual(labDefault.getLocation(), "Up")
		self.assertEqual(lab.getLocation(), "Flipways")
	def testSettaID(self):
		labDefault.settaID(2)
		lab.settaID(3)
		self.assertEqual(labDefault.gettaID(), 2)
		self.assertEqual(lab.gettaID(), 3)

if __name__ == '__main__':
unittest.main()