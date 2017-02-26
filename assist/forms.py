from django.forms import ModelForm
from django import forms
from .models import User , Announcement
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
    remember = forms.BooleanField(label="Remember Me?",required=False)
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_action   = 'login'
    helper.add_input(Submit('submit', 'login', css_class='btn-primary'))

# class AnnouncementForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(AnnouncementsForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper(self)
#         self.helper.form_method = 'POST'
#         self.helper.add_input(Submit('submit', 'go', css_class='btn-primary'))
#     class Meta:
#         model = Announcements
#         exclude = ['author','course']
class AnnouncementForm(forms.Form):
    title       = forms.CharField(label="Title", required=True, widget=forms.TextInput)
    description = forms.CharField(label="Description", required=True, widget=forms.Textarea)
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
       
