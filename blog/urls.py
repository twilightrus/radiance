from django.conf.urls import url
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from .views import *


app_name = "blog"

urlpatterns = [
    path('', lambda request: redirect('blog:page', '1'), name='index'),
    url(r'^page/(?P<page>[0-9]+)/$', login_required(ArticleListView.as_view(), redirect_field_name=None), name='page'),
    url(r'^(?P<pk>[0-9]+)/$', login_required(ArticleDetailView.as_view(), redirect_field_name=None), name='detail'),
    ]
