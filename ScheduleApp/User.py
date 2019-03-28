# test


class User:
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

    # TODO: Define method stubs for unit testing

    def __methodName__(self):
        # Format for stubs
        return 0

    #Default Constructor
    def __init__(self):

        pass

    #Parameterized Constructor


    # Create a new User object from a string containing all the fields separated by commas.
    # The string is formated as: the permission = [],username = "",password = "",databaseID = 0,email = "",firstName = "",lastName = "",contactPhone = "",officePhone = "",extension = ""
    # Example: ""
    def fromString(self):
        # code
        return 0

    # Returns a string that has all the fields a User has.
    # Currently meant to function with fromString.
    # May want an alternative method for printing out the User in a pretty way.
    def toString(self):
        pass

    # Update all of User's fields within the database.
    def updateDataBase(self):
        # code
        return 0

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
