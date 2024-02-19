from django import forms
from django.core.validators import EmailValidator


class EmailForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField(validators=[EmailValidator()])
    message = forms.CharField(widget=forms.Textarea)
