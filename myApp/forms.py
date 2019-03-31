from django import forms


class InputForm(forms.Form):
    command = forms.CharField()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
