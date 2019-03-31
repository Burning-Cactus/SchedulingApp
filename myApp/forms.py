from django import forms


class InputForm(forms.Form):
    command = forms.CharField()
