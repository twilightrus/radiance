from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect

from .forms import RegistrationForm, AuthForm

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

from django.urls import reverse

from django.views.generic import View, CreateView, FormView


class AuthenticatedMixin(object):
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('blog:index')
        return super().dispatch(*args, **kwargs)


class RegisterView(AuthenticatedMixin, FormView):

    template_name = 'registration/register.html'
    form_class = RegistrationForm

    def form_valid(self, form):
        user = User.objects.create_user(username=form.cleaned_data.get('login'),
                                        password=form.cleaned_data.get('password'))
        login(self.request, user)
        return redirect('blog:index')


class AuthView(AuthenticatedMixin, FormView):

    template_name = 'auth/auth.html'
    form_class = AuthForm

    def form_valid(self, form):

        login(self.request, form.user)
        return redirect('blog:index')


def logout_user(request):

    logout(request)
    return redirect('users:auth')