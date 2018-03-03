from django.forms import CharField, Form, PasswordInput, ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils.html import strip_tags

from hooli.forms import ErrorForm
from .models import Comment, Like


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'article']


class ArticleLikeForm(ModelForm):
    class Meta:
        model = Like
        fields = ['article']


class CommentLikeForm(ModelForm):
    class Meta:
        model = Like
        fields = ['comment']
