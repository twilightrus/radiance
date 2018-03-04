from django.forms import CharField, Form, PasswordInput, ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils.html import strip_tags

from radiance.forms import ErrorForm
from .models import Comment, Like


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'article']


class DeleteCommentForm(ModelForm, ErrorForm):
    class Meta:
        model = Comment
        fields = ['id']

    #def __init__(self, *args, **kwargs):
    #    self.user = kwargs.pop('user', None)
    #    super(DeleteCommentForm, self).__init__(*args, **kwargs)

    def clean(self):
    #    comment = Comment.objects.filter(pk=self.cleaned_data.get('id'), user=self.user)
        print(self.cleaned_data)
    #   print(comment.exists())
    #   if not comment.exists():
    #        raise forms.ValidationError('Not allowed!')
    #    else:
    #        comment.delete()

        return self.cleaned_data


class ArticleLikeForm(ModelForm):
    class Meta:
        model = Like
        fields = ['article']


class CommentLikeForm(ModelForm):
    class Meta:
        model = Like
        fields = ['comment']
