

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

    def updateDataBase(self):
        # code
        return 0

    def setClassNumber(self, value):
        self.classNumber = value
        return

    def get_class_number(self):
        return self.classNumber

    def set_time(self, value):
         self.time = value
         return

    def get_time(self):
        return self.time

    def set_location(self, value):
        self.location = value
        return

    def get_location(self):
        return self.location
    #end