from django import forms

class commentinputforme(forms.Form):
    text = forms.CharField(label='текст', max_length=500, required=True)


class ProfileEditingForm(forms.Form):
    email = forms.EmailField(label='email', max_length=50, required=True)
    name = forms.CharField(label='имя', max_length=12, required=True)
