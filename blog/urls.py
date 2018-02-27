from django.conf.urls import url
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from .views import *
from . import views


app_name = "blog"

urlpatterns = [
    path('', login_required(ArticleListView.as_view(), redirect_field_name=None), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', login_required(ArticleDetailView.as_view(), redirect_field_name=None), name='detail'),
    #url(r'^comments/add/$' , login_required(CreateCommentView.as_view(), redirect_field_name=None), name='comment_add'),
    ]
