from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from .forms import RegistrationForm, AuthForm

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.urls import reverse


def register(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("blog:index"))

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data.get('login'),
                                            password=form.cleaned_data.get('password'))
            login(request, user)
            return HttpResponseRedirect(reverse("blog:index"))

    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def auth(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("blog:index"))

    if request.POST:
        form = AuthForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return HttpResponseRedirect(reverse("blog:index"))

    else:
        form = AuthForm()

    return render(request, 'auth/auth.html', {'form': form})


def logout_user(request):

    logout(request)
    return HttpResponseRedirect(reverse("users:auth"))
