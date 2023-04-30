from django import forms

class commentinputforme(forms.Form):
    name = forms.CharField(label='имя', max_length=21, required=True)
    text = forms.CharField(label='текст', max_length=500, required=True)