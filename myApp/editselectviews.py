from django.shortcuts import render,redirect
from django.views import View
from myApp.models import Terminal
from django.http import HttpRequest, HttpResponse
from .forms import InputForm, LoginForm
from .models import USER

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
