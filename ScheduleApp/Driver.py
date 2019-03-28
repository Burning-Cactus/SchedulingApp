from myApp.views import Interface
from myApp.models import Terminal
from SchedulingApp import User


def main(self):
    
    user = None

    # render the html page
    Interface.get()

    Interface.echo("Please use login command: login(username, password)")
    
    # start a login loop
    while(user == none):

        response = Interface.post()
        
        if(response.isinstance(User)):
                user = response

    # create login 'session' persay
    while(user != None):

        response = Interface.post()

        # maybe do something with the response ex. set user to None if logout was called


        

