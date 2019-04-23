from django.test import Client

class CreateCourseTest():
    c = Client()
    c.get('/base/')