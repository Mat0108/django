from django import forms

class NameForm(forms.Form):
    mail = forms.CharField(label='Mail', max_length=100)
    password = forms.CharField(label='Password ', max_length=100)