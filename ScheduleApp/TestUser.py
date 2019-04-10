import unittest
from ScheduleApp import User


class TestUser(unittest.TestCase):
    
    def test_constructor(self):
        with self.asserRaises(ValueError):
            pass
    
    def test_fromString(self):
        userString = "[1,2]$username$password$45$email@email.com$first name$last name$4142223333"

        user = User.fromString(userString)
        
        self.assertEquals([1,2], user.permission)
        self.assertEquals('username', user.username)
        self.assertEquals('password', user.password)
        self.assertEquals(45, user.databaseID)
        self.assertEquals("email@emai.com", user.email)
        self.assertEquals("first name", user.firstName)
        self.assertEquals("last name", user.lastName)
        self.assertEquals("4142223333", user.contactPhone)
        
        userString = "[1,2]$username$password$45$email@email.com$first name$last name$4142223333$4142221111"
        user.fromString(userString)
        
        self.assertEquals([1,2], user.permission)
        self.assertEquals('username', user.username)
        self.assertEquals('password', user.password)
        self.assertEquals(45, user.databaseID)
        self.assertEquals("email@emai.com", user.email)
        self.assertEquals("first name", user.firstName)
        self.assertEquals("last name", user.lastName)
        self.assertEquals("4142223333", user.contactPhone)
        self.assertEquals("4142221111", user.contactPhone)
        
        userString = "[1]$username$password$45$email@email.com$first name$last name$4142223333$4142221111$325"
        user.fromString(userString)
        
        self.assertEquals([1], user.permission)
        self.assertEquals('username', user.username)
        self.assertEquals('password', user.password)
        self.assertEquals(45, user.databaseID)
        self.assertEquals("email@emai.com", user.email)
        self.assertEquals("first name", user.firstName)
        self.assertEquals("last name", user.lastName)
        self.assertEquals("4142223333", user.contactPhone)
        self.assertEquals("4142221111", user.contactPhone)
        self.assertEquals("325", user.contactPhone)
        
    def test_toString(self):
        user = User([1,2], "username", "password", 45, "email@email.com", "first name", "last name", "4142223333")
        userString = user.toString()
        
        self.assertEquals("[1,2]$username$password$45$email@email.com$first name$last name$4142223333", userString)
        
        user = User([1], "username", "password", 45, "email@email.com", "first name", "last name", "4142223333", "4142221111")
        userString = user.toString()
        
        self.assertEquals("[1]$username$password$45$email@email.com$first name$last name$4142223333$4142221111", userString)
        
        user = User([1], "username", "password", 45, "email@email.com", "first name", "last name", "4142223333", "4142221111", "325")
        userString = user.toString()
        
        self.assertEquals("[1]$username$password$45$email@email.com$first name$last name$4142223333$4142221111$325", userString)
        
        
    def test_getPermission(self):
        user = User(permission = [1,3])
        self.assertEquals([1,3], user.getPermission())
        
        user = User(permission = None)
        self.assertEquals(None, user.getPermission())
        
        user = User(permission = [])
        self.assertEquals(None, user.getPermission())
        
    def test_getUsername(self):
        user = User(username = "username")
        self.assertEquals("username", user.getUsername())
        
        user = User(username = None)
        self.assertEquals(None, user.getUsername())
        
    def test_getPassword(self):
        user = User(password = "password")
        self.assertEquals("password", user.getPassword())
        
        user = User(password = None)
        self.assertEquals(None, user.getPassword())
        
    def test_getFirstName(self):
        user = User(firstName = "John")
        self.assertEquals("John", user.getFirstName())
        
        user = User(firstName = None)
        self.assertEquals(None, user.getFirstName())
        
    def test_getLastName(self):
        user = User(lastName = "Doe")
        self.assertEquals("Doe", user.getLastName())
        
        user = User(lastName = None)
        self.assertEquals(None, user.getLastName())
        
    def test_getEmail(self):
        user = User(email = "email@email.com")
        self.assertEquals("email@email.com", user.getEmail())
        
        user = User(email = None)
        self.assertEquals(None, user.getEmail())
        
    def test_getContactPhone(self):
        user = User(contactPhone = "2223334444")
        self.assertEquals("2223334444", user.getContactPhone())
        
        user = User(contactPhone = None)
        self.assertEquals(None, user.getContactPhone())
        
    def test_getOfficePhone(self):
        user = User(officePhone = "2223334444")
        self.assertEquals("2223334444", user.getOfficePhone())
        
        user = User(officePhone = None)
        self.assertEquals(None, user.getOfficePhone())
        
    def test_getExtension(self):
        user = User(extension = "325")
        self.assertEquals("325", user.getExtension())
        user = User(extension = None)
        self.assertEquals(None, user.getExtension())
        
    def test_getDatabaseID(self):
        user = User(databaseID = 12)
        self.assertEquals(12, user.getDatabaseID())
        
        user = User(databaseID = None)
        self.assertEquals(None, user.getDatabaseID())
        
    def test_setPermission(self):
        user = User()
        
        user.setPermission([1])
        self.assertEquals([1], user.permission)
        
        user.setPermission([1,2])
        self.asserEquals([1,2], user.permission)
        
        with self.asserRaises(ValueError):
            user.setPermission(True)
            user.setPermission(1)
            user.setPermission(1,"this")
            user.setPermission("this")
            user.setPermission({})
            user.setPermission(35)
            user.setPermission('raw')
            user.setPermission(4.5)
            user.setPermission([42])
            user.setPermission([-42])
    
    def test_setUsername(self):
        user = User()
        
        user.setUsername("username")
        self.assertEquals("username", user.username)
        
        with self.asserRaises(ValueError):
            user.setUsername(True)
            user.setUsername(1)
            user.setUsername(1,"this")
            user.setUsername({})
            user.setUsername(35)
            user.setUsername(4.5)
            user.setUsername([42])
    
    def test_setPassword(self):
        user = User()
        
        user.setPassword("password")
        self.assertEquals("password", user.password)
        
        with self.asserRaises(ValueError):
            user.setPassword(True)
            user.setPassword(1)
            user.setPassword(1,"this")
            user.setPassword({})
            user.setPassword(35)
            user.setPassword(4.5)
            user.setPassword([42])
    
    def test_setEmail(self):
        user = User()
        
        user.setEmail("email@email.com")
        self.assertEquals("email@email.com", user.emai)
        
        with self.asserRaises(ValueError):
            user.setEmail(True)
            user.setEmail(1)
            user.setEmail(1,"this")
            user.setEmail({})
            user.setEmail(35)
            user.setEmail(4.5)
            user.setEmail([42])
            user.setEmail('this')
            user.setEmail("this@")
            user.setEmail("this@ ")
            user.setEmail("@gmail.com")
    
    def test_setFirstName(self):
        user = User()
        
        user.setFirstName("John")
        self.assertEquals("John", user.firstName)
        
        with self.asserRaises(ValueError):
            user.setFirstName(True)
            user.setFirstName(1)
            user.setFirstName(1,"this")
            user.setFirstName({})
            user.setFirstName(35)
            user.setFirstName(4.5)
            user.setFirstName([42])
    
    def test_setLastName(self):
        user = User()
        
        user.setLastName("John")
        self.assertEquals("John", user.lastName)
        
        with self.asserRaises(ValueError):
            user.setLastName(True)
            user.setLastName(1)
            user.setLastName(1,"this")
            user.setLastName({})
            user.setLastName(35)
            user.setLastName(4.5)
            user.setLastName([42])
    
    def test_setContactPhone(self):
        user = User()
        
        user.setContactPhone("2223334444")
        self.assertEquals("2223334444", user.officePhone)
        
        with self.asserRaises(ValueError):
            user.setContactPhone(True)
            user.setContactPhone(1)
            user.setContactPhone(1,"this")
            user.setContactPhone({})
            user.setContactPhone(35)
            user.setContactPhone(4.5)
            user.setContactPhone([42])
            user.setContactPhone("222       333334444444")
            user.setContactPhone("number")
            user.setContactPhone(2223334444)
            
    
    def test_setOfficePhone(self):
        user = User()
        
        user.setOfficePhone("2223334444")
        self.assertEquals("2223334444", user.officePhone)
        
        with self.asserRaises(ValueError):
            user.setOfficePhone(True)
            user.setOfficePhone(1)
            user.setOfficePhone(1,"this")
            user.setOfficePhone({})
            user.setOfficePhone(35)
            user.setOfficePhone(4.5)
            user.setOfficePhone([42])
            user.setOfficePhone("222       333334444444")
            user.setOfficePhone("number")
            user.setOfficePhone(2223334444)
    
    def test_setExtension(self):
        user = User()
        
        user.setExtension("325")
        self.assertEquals("325", user.extension)
        
        with self.asserRaises(ValueError):
            user.setExtension(True)
            user.setExtension(1)
            user.setExtension(1,"this")
            user.setExtension({})
            user.setExtension(35)
            user.setExtension(4.5)
            user.setExtension([42])
            user.setExtension("222       333334444444")
            user.setExtension("number")
            user.setExtension(325)
        
        
        
if __name__ == '__main__':
    unittest.main()
