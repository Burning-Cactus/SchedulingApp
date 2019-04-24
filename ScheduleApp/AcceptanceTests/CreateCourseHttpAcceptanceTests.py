from django.test import Client
from django.test import TestCase
from myApp.models import USER


class CreateCourseTest(TestCase):
    
    def setup(self):
        self.user = USER.objects.create(permission=[4], username="john", password="test", email="john@this.com",
                                        firstName="john", lastName="flupper", contactPhone="2628889765",
                                        officePhone="2624235436", extension="151")
    
    # Test to make sure the url is set correctly
    def testUrl(self):    
        c = Client()
        # response = c.post('/login/', {'username': 'john', 'password': 'smith'})
        # response.status_code
        # response = c.get('/createCourse/')
        # response.content
        response = c.post('/createCourse/')
        url = response.redirect_chain
        self.assertEquals(url, '/createCourse/')
       
    def testFunc(self):
        c = Client()
        
