from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse, resolve
from django.shortcuts import redirect


class RemoveNextMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.path == reverse(settings.LOGIN_URL) and 'next' in request.GET:
            return redirect(settings.LOGIN_URL)


class LoginRequiredMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if resolve(request.path).app_name == 'blog' and not request.user.is_authenticated:
            return redirect(settings.LOGIN_URL)
