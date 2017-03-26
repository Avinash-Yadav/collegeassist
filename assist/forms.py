from django.forms import ModelForm
from django import forms
from .models import User , Announcement, Student, Feedback
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)
from django.contrib.auth.forms import UserCreationForm 
class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('submit', 'register'))
    class Meta:
        model  = User
        fields = ['email','first_name','last_name','password1','password2']
    
    def save(self,commit = True):   
        user = super(RegisterForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user

class ForgetPasswordForm(forms.Form):
    email = forms.CharField(label="Email", required=True)
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_action   = 'forgetpassword'
    helper.add_input(Submit('submit', 'submit', css_class='btn-primary'))

class LoginForm(forms.Form):
    email = forms.CharField(label="Email", required=True)
    password = forms.CharField(label="Password", required=True, widget=forms.PasswordInput)
    remember = forms.BooleanField(label="Remember Me?",required=False)
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_action   = 'login'
    helper.add_input(Submit('submit', 'login', css_class='btn-primary'))

class AvatorForm(forms.Form):
    avator       = forms.FileField(label="Upload avator",widget=forms.ClearableFileInput(attrs={'multiple': True}),required=False)
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_action   = 'profile'
    helper.add_input(Submit('submit', 'submit', css_class='btn-primary'))

class AnnouncementForm(forms.Form):
    title       = forms.CharField(label="Title", required=True, widget=forms.TextInput)
    description = forms.CharField(label="Description", required=True, widget=forms.Textarea)
    files       = forms.FileField(label="Files",widget=forms.ClearableFileInput(attrs={'multiple': True}),required=False)
    helper = FormHelper()
    helper.form_method = 'POST'
    # helper.form_action   = 'login'
    helper.add_input(Submit('submit', 'submit', css_class='btn-primary'))

class FeedbackForm(forms.Form):
    title       = forms.CharField(label="Title", required=True, widget=forms.TextInput)
    feedback    = forms.CharField(label="Feedback", required=True, widget=forms.Textarea)
    files       = forms.FileField(label="Files",widget=forms.ClearableFileInput(attrs={'multiple': True}),required=False)
    helper = FormHelper()
    helper.form_method = 'POST'
    # helper.form_action   = 'login'
    helper.add_input(Submit('submit', 'submit', css_class='btn-primary'))

class MaterialForm(forms.Form):
    title       = forms.CharField(label="Title", required=True, widget=forms.TextInput)
    files       = forms.FileField(label="Files",widget=forms.ClearableFileInput(attrs={'multiple': True}))
    helper = FormHelper()
    helper.form_method = 'POST'
    # helper.form_action   = 'login'
    helper.add_input(Submit('submit', 'submit', css_class='btn-primary'))

class ExamPaperForm(forms.Form):
    files       = forms.FileField(label="Files",widget=forms.ClearableFileInput(attrs={'multiple': True}))
    term        = forms.ChoiceField(label="Exam-type", required=True, widget=forms.RadioSelect,choices=(('M', 'Mid-Sem',), ('E', 'End-Sem',)))
    helper = FormHelper()
    helper.form_method = 'POST'
    # helper.form_action   = 'login'
    helper.add_input(Submit('submit', 'submit', css_class='btn-primary'))

# class ProfileForm(forms.Form): # to be done
#     first_name   = forms.CharField(label='First Name',required=True,widget=forms.TextInput)
#     last_name    = forms.CharField(label='Last Name',required=True,widget=forms.TextInput)
#     email        = forms.EmailField(required=True,widget=forms.EmailInput)
#     semester     = forms.CharField(label='Semester',required=False,widget=forms.NumberInput)
#     registration_no = forms.CharField(Label='Registration No',widget=forms.TextInput)
#     helper       = FormHelper()
#     helper.form_method = 'POST'
#     helper.form_action = 'profile'
#     helper.add_input(Submit('submit','submit',css_class='btn-primary'))
