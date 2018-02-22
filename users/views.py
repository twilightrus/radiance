from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect

from .forms import RegistrationForm, AuthForm

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

from django.urls import reverse

from django.views.generic import View, CreateView


class RegisterView(CreateView):

    template_name = 'registration/registration.html'
    form_class = RegistrationForm

    def form_valid(self, form):
        form.instance.login = self.request.login
        form.instance.password = self.request.password
        form.instance.password_verify = self.request.password_verify

        return super(RegisterView, self)


def auth(request):

    if request.user.is_authenticated:
        return redirect('blog:index')

    if request.POST:
        form = AuthForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return redirect('blog:index')

    else:
        form = AuthForm()

    return render(request, 'auth/auth.html', {'form': form})


def logout_user(request):

    logout(request)
    return redirect('users:auth')