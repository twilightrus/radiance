from django.conf.urls import url

from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^(?P<article_id>[0-9]+)/$', views.detail, name='detail'),
    ]
