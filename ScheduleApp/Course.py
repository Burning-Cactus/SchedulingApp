

class Course:
    databaseID = 0
    name = ""
    courseNumber = 0
    classNumber = 0
    labList = []
    time = ""
    location = ""

    def __init__(self):
        pass

    def __init__(self, databaseID, name, courseNumber, classNumber, labList, time, location):
        self.databaseID = databaseID
        self.name = name
        self.courseNumber = courseNumber
        self.classNumber = classNumber
        self.labList = labList
        self.time = time
        self.location = location

    def setDataBaseID(self, value):
        self.databaseID = value
        return

    def getDataBaseID(self):
        return self.databaseID

    def setName(self, value):
        self.name = value
        return

    def getName(self):
        return self.name

    def fromString(self, formatedString):
        params = formatedString.split(",")
        params[0] = params[0][1:-1]
        self.name = params[0].split(" ")
        self.courseNumber = params[1]
        self.classNumber = params[2]
        labs = params[3].split(" ")
        self.labList = labs
        self.time = params[4]
        self.location = params[5]
        return

    def setClassNumber(self, value):
        self.classNumber = value
        return

    def getClassNumber(self):
        return self.classNumber

    def setTime(self, value):
        self.time = value
        return

    def getTime(self):
        return self.time

    def setLocation(self, value):
        self.location = value
        return

    def getLocation(self):
        return self.location

    def addLab(self, value):
        self.labList = self.labList+value

    #end