from django import forms


class InputForm(forms.Form):
    command = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    command.label = "OOPLA_SEVER: \\USER>"


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
