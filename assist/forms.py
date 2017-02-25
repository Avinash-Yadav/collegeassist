from django.froms import ModelForm
from django import forms
from .models import User
class RegisterForm(forms.ModelForm):
    class Meta:
        model  = User
        fields = ['first_name','last_name','email','registration_no','']
