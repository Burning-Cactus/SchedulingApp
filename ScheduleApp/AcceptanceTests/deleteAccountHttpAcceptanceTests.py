from django.test import Client, TestCase

class deleteAccountHttpAcceptanceTest():

    #Tests a properly used delete page
        #returns a status_code equal to 200
    def test1(self):
        c = Client()
        response = c.post('/delete/', {'username': 'john', 'password': 'smith'})
        response = c.get('/customer/details/')
        TestCase.assertEqual(response.status_code, 200)

        #check databaseID
        #looking at session and make sure it is equal to something?

        TestCase.assertEqual()


