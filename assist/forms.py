from django.forms import ModelForm
from django import forms
from .models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)
class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('submit', 'register'))
    class Meta:
        model  = User
        fields = ['email','password','first_name','last_name']

class LoginForm(forms.Form):
    email = forms.CharField(label="Email", required=True)
    password = forms.CharField(label="Password", required=True, widget=forms.PasswordInput)
    remember = forms.BooleanField(label="Remember Me?")
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_action   = 'login'
    helper.add_input(Submit('submit', 'login', css_class='btn-primary'))
        
