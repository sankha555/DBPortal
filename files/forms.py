from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import File
from users.models import Profile
from allauth.socialaccount.forms import SignupForm
from allauth.account.forms import LoginForm
from django.core import validators

class FileUploadForm(forms.ModelForm):
    botcatcher = forms.FileField(required = False, widget = forms.HiddenInput,
                                 validators = [validators.MaxLengthValidator(0)])

    class Meta:
        model = File
        fields = ['fname', 'doc']

class SearchUIDForm(forms.Form):
    botcatcher = forms.CharField(required = False, widget = forms.HiddenInput,
                                 validators = [validators.MaxLengthValidator(0)])
    uid = forms.CharField(max_length=12)
    fields = ['uid']

class MailContentForm(forms.Form):
    subject = forms.CharField(max_length = 20)
    content = forms.CharField(max_length = 264)

    fields = ['subject', 'content']

class AddDberForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['uid', 'name', 'dob', 'gender', 'city', 'state']

class SearchCityStaffForm(forms.Form):

    city = forms.CharField(max_length = 20)
    fields = ['city']
