from django.test import Client
c = Client()
response = c.post('/delete/', {'username': 'john', 'password': 'smith'})
response = c.get('/customer/details/')
