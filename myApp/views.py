from django.shortcuts import render,redirect
from django.views import View
from myApp.models import Terminal
from django.http import HttpRequest, HttpResponse
from .forms import InputForm, LoginForm
from .models import USER
# Create your views here.
class Shell(View):
    response = [""]
    terminalInstance = Terminal()

    def get(self, request):
        return render(request, 'shell/index.html', {"message": Shell.response, "user": ""})

    def post(self, request):
        if request.method == 'POST':
            form = InputForm(request.POST)
            if form.is_valid():

                userInput = form.cleaned_data['command']

                terminalResponse = Shell.terminalInstance.command(userInput)

                if isinstance(terminalResponse, list):
                    Shell.response.extend(terminalResponse)
                else:
                    Shell.response.append(terminalResponse)

        return render(request, 'shell/index.html', {"message": Shell.response, "user": Shell.terminalInstance.username})

class createAccount(View):

    def get(self, request):
        return render(request, 'shell/createAccount.html')

    def post(self, request):
        username = request.POST['UserName']
        password = request.POST['Password']
        permission = request.POST['Permission']
        email = request.POST['Email']
        firstName = request.POST['FirstName']
        lastName = request.POST['LastName']
        contactPhone = request.POST['ContactPhone']
        officePhone = request.POST['OfficePhone']
        extension = request.POST['Extension']
        response = Terminal.createAccount(permission, username, password, email, firstName, lastName, contactPhone, officePhone, extension)
        if response is not "New user created":
            return redirect('createAccountError/')
        else:
            return redirect('homepagee/')
        # placeholder^
class createAccountError(View):

    def get(self, request):
        return render(request, 'shell/createAccountError.html')
    def post(self, request):
        return render(request, 'shell/createAccountError.html')

class editAccount(View):

    def get(self, request):
        return render(request, 'shell/editAccount.html')

    def post(self, request):
        response = Terminal.editAccount(request.session['editID'], request.POST['Permission'], request.POST['UserName'],
                                        request.POST['Password'], request.POST['Email'], request.POST['FirstName'],
                                        request.POST['LastName'], request.POST['ContactPhone'], request.POST['OfficePhone'],
                                        request.POST['Extension'])
        if response == "User account updated":
            return render(request, ['http://127.0.0.1:8000/home'])
        if response == "User does not exist":
            return render(request, ['shell/editAccountError.html'])
        else:
            return render(request, ['shell/editAccountError.html'])

class editSelect(View):

    def get(self, request):
        return render(request, 'shell/editSelect.html')

    def post(self, request):
        try:
            if USER.objects.get(request.POST['UserID']):
                request.session['editID'] = request.POST['UserID']
                return render(request, 'shell/editAccount.html')
        except USER.DoesNotExist:
            return render(request, 'shell/editAccountError.html')


