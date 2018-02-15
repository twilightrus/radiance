from django.forms import CharField, Form, PasswordInput

from django import forms

from django.contrib.auth.models import User

from django.contrib.auth import authenticate


class ErrorForm:

    def get_errors(self):

        """ Return list of validation errors or False, if errors isn't exists. """

        errors_list = []
        for _, errors in self.errors.items():
            for error in errors:
                errors_list.append(error)
        if len(errors_list) <= 0:
            return False
        else:
            return errors_list

    def is_has_errors(self):

        """ Returns True if form has errors and False if errors isn't exists """

        if len(self.errors) > 0:
            return True

        return False


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

        try:
            user = User.objects.get(username=self.cleaned_data.get('login'))
            if user is not None:
                raise forms.ValidationError('Your username is already used!')

        except User.DoesNotExist:
            pass

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
