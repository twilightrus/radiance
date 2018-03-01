from django.forms import CharField, Form, PasswordInput, ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils.html import strip_tags

from hooli.forms import ErrorForm
from .models import Comment


class CommentForm(ModelForm, ErrorForm):
    class Meta:
        model = Comment
        fields = ['content', 'article_id']
