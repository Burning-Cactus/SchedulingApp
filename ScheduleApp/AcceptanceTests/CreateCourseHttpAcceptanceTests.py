from django.test import Client
from django.test import TestCase

class CreateCourseTest(TestCase):
    c = Client()
    response = c.post('/login/', {'username': 'john', 'password': 'smith'})
    response.status_code
    response = c.get('/createCourse/')
    response.content
