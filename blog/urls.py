from django.conf.urls import url

from django.urls import path

from django.contrib.auth.decorators import login_required

from . import views

from .views import ArticleListView, ArticleDetailView

app_name = "blog"

urlpatterns = [
    path('', login_required(ArticleListView.as_view()), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', ArticleDetailView.as_view(), name='detail'),
    ]
