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
    url(r'^(?P<pk>[0-9]+)/comments/', login_required(CommentsView.as_view(), redirect_field_name=None),
        name='comments_get'),
    url(r'^(?P<pk>[0-9]+)/likes/', login_required(LikesView.as_view(), redirect_field_name=None),
        name='likes_get'),
    url(r'^comments/add/$', login_required(CommentCreateView.as_view(), redirect_field_name=None), name='comment_add'),
    url(r'^comments/(?P<pk>[0-9]+)/edit$', login_required(CommentEditView.as_view(), redirect_field_name=None), name='comment_edit'),
    url(r'^comments/delete/$', login_required(CommentDelete.as_view(), redirect_field_name=None), name='comment_delete'),
    url(r'^likes/articles/add/$', login_required(ArticleLikeCreateView.as_view(), redirect_field_name=None), name='like_article_add'),
    url(r'^likes/comments/add/$', login_required(CommentLikeCreateView.as_view(), redirect_field_name=None), name='like_comment_add'),
    ]
