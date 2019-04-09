

class Lab:
    labID = 0
    name = ""
    courseID = 0
    classNumber = 0
    time = ""
    location = ""
    labNumber=0




    def getDataBaseID(self, value):

        return self.labID

    def __init__(self,ID,name,course,classnr,time,location,labnr):
        labID=ID
        name=name
        courseID=course
        classNumber=classnr
        time=time
        location=location
        labNumber=labnr

        return 0


    def toString(self):
        return (self.labID+","+self.name+","+self.labNumber+","+self.courseID+","+self.time+","+self.location)

    def getName(self):
        return self.name

    def setName(self, x):
        self.name = x
        return 0

    def getTime(self):
        return self.time

    def setTime(self, x):
        self.time =x
        return 0

    def getLocation(self):
        return self.location

    def setLocation(self, x):
        self.location = x
        return 0

    def getCourseID(self):
        return self.courseID

    def setCourseID(self,x):
        self.courseID=x
        return 0

    def setLabNr(self,x):
        self.labNumber=x
        return 0

    def getLabNr(self):
        return self.labNumber

    def getClassNr(self):
        return self.classNumber

    def setClassNr(self,x):
        self.classNumber=x
        return 0

