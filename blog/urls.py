from django.urls import path

from blog.views import (ArticleListView, ArticleDetailView, ArticleLikeCreateView,
                        CommentsView, CommentEditView, CommentCreateView,
                        CommentDelete, CommentLikeCreateView, LikesView)

app_name = "blog"

urlpatterns = [
    path('', ArticleListView.as_view(), name='index'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='detail'),
    path('<int:pk>/comments/', CommentsView.as_view(), name='comments_get'),
    path('<int:pk>/likes/', LikesView.as_view(), name='likes_get'),
    path('comments/add/', CommentCreateView.as_view(), name='comment_add'),
    path('comments/<int:pk>/edit/', CommentEditView.as_view(), name='comment_edit'),
    path('comments/delete/', CommentDelete.as_view(), name='comment_delete'),
    path('likes/articles/add/', ArticleLikeCreateView.as_view(), name='like_article_add'),
    path('likes/comments/add/', CommentLikeCreateView.as_view(), name='like_comment_add'),
    ]
