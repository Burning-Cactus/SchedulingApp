# Description of User:
#Made by John and Andy

class User(object):
    permission = []
    username = ""
    password = ""
    databaseID = 0
    email = ""
    firstName = ""
    lastName = ""
    contactPhone = ""
    officePhone = ""
    extension = ""

    #Default Constructor
    def __init__(self):
        #all the variables default to the values above...
        pass

    #Parameterized Constructor
    def __init__(self, permission, username, password, databaseID, email, firstName, lastName, contactPhone, officePhone, extension):
        self.permission=permission
        self.username=username
        self.password=password
        self.databaseID=databaseID
        self.email=email
        self.firstName=firstName
        self.lastName=lastName
        self.contactPhone=contactPhone
        self.officePhone=officePhone
        self.extension=extension

        # Parameterized Constructor
    def __call__(self, permission, username, password, databaseID, email, firstName, lastName, contactPhone, officePhone, extension):
        self.permission = permission
        self.username = username
        self.password = password
        self.databaseID = databaseID
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.contactPhone = contactPhone
        self.officePhone = officePhone
        self.extension = extension

    # Create a new User object from a string containing all the fields separated by commas.
    # The string is formated as: the permission,username,password,databaseID,email,firstName,lastName,contactPhone,officePhone,extension
    # Example: "(1 2 3),usermane,pass1234,1337,test@gmail.com,first,last,9-(123)-123-1234,1-800-crayonSLAYER,247"
    #TODO: Require that none of these fields may contain a comma or else this won't work. /n may be a better delimiter
    def fromString(self, formatedString):
        params = formatedString.split(",")      #splits the contents of the string into elements of an array
        params[0] = params[0][1:-1]             #removes the first and last character in (example) "(0 1)" -> "0 1"
        self.permission = params[0].split(" ")
        self.username = params[1]
        self.password = params[2]
        self.databaseID = params[3]
        self.email = params[4]
        self.firstName = params[5]
        self.lastName = params[6]
        self.contactPhone = params[7]
        self.officePhone = params[8]
        self.extension = params[9]
        return 0

    # Returns a string that has all the fields a User has.
    # Currently meant to function with fromString.
    # May want an alternative method for printing out the User in a pretty way.
    def toString(self):
        #can't print an array, grab it's contents
        intermediate = "("
        for i in permission:
            intermediate += i + " "
        return intermediate+"),"+self.username+","+self.password+","+self.databaseID+","+self.email+","+self.firstName+","+self.lastName+","+self.contactPhone+","+self.officePhone+","+self.extension

    #Setters
    def setPermisson(self, permissionList):
        self.permission=permissionList

    def setUsername(self, username):
        self.username=username
    
    def setPassword(self, password):
        self.password=password

    def setDatabaseID(self, databaseID):
        self.databaseID=databaseID
    
    def setEmail(self, email):
        self.email=email
    
    def setFirstName(self, firstName):
        self.firstName=firstName
    
    def setLastName(self, lastName):
        self.lastName=lastName
    
    def setContactPhone(self, contactPhone):
        self.contactPhone=contactPhone
    
    def setOfficePhone(self, officePhone):
        self.officePhone=officePhone
    
    def setExtension(self, extension):
        self.extension=extension

    #Getters
    def getPermisson(self):
        return self.permission

    def getUsername(self):
        return self.username
    
    def getPassword(self):
        return self.password

    def getDatabaseID(self):
        return self.databaseID
    
    def getEmail(self):
        return self.email
    
    def getFirstName(self):
        return self.firstName
    
    def getLastName(self):
        return self.lastName
    
    def getContactPhone(self):
        return self.contactPhone
    
    def getOfficePhone(self):
        return self.officePhone
    
    def getExtension(self):
        return self.extension
