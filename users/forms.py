from django.forms import CharField, Form, PasswordInput
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from radiance.forms import ErrorForm


class RegistrationForm(Form, ErrorForm):
    login = CharField(
        label='Login',
        min_length=4,
        max_length=50)

    password = CharField(
        label='Password',
        min_length=4,
        max_length=50,
        widget=PasswordInput())

    password_verify = CharField(
        label='Password (verify)',
        min_length=4,
        max_length=50,
        widget=PasswordInput())

    def clean(self):

        if self.cleaned_data.get('password') != self.cleaned_data.get('password_verify'):
            raise forms.ValidationError('Passsword != Verify password!')

        user = User.objects.filter(username=self.cleaned_data.get('login')).exists()
        if user is True:
            raise forms.ValidationError('Your username is already used!')

        return self.cleaned_data


class AuthForm(Form, ErrorForm):
    login = CharField(
        label='Login',
        min_length=4,
        max_length=50)

    password = CharField(
        label='Password',
        min_length=4,
        max_length=50,
        widget=PasswordInput())

    def clean(self):

        self.user = authenticate(username=self.cleaned_data.get('login'), password=self.cleaned_data.get('password'))
        if self.user is None:
            raise forms.ValidationError('Invalid login or password!')
        return self.cleaned_data
