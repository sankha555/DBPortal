from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from allauth.socialaccount.forms import SignupForm
from allauth.account.forms import LoginForm
from django.core import validators

class RegForm(UserCreationForm):
    email = forms.EmailField()
    botcatcher = forms.CharField(required = False, widget = forms.HiddenInput,
                                 validators = [validators.MaxLengthValidator(0)])

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'botcatcher']


class StaffUpdateForm(forms.ModelForm):
    botcatcher = forms.CharField(required = False, widget = forms.HiddenInput,
                                 validators = [validators.MaxLengthValidator(0)])

    class Meta:
        model = Profile
        fields = ['uid', 'name', 'dob', 'gender', 'state', 'city', 'botcatcher']

class DberUpdateForm(forms.ModelForm):
    botcatcher = forms.CharField(required = False, widget = forms.HiddenInput,
                                 validators = [validators.MaxLengthValidator(0)])

    class Meta:
        model = Profile
        fields = ['name', 'dob', 'gender', 'state', 'city', 'botcatcher']

class EmailChangeForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email']
