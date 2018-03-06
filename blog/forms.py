from django import forms
from django.forms import Form, ModelForm

from radiance.forms import ErrorForm
from .models import Comment, Like


class CommentForm(ModelForm, ErrorForm):
    class Meta:
        model = Comment
        fields = ('content', 'article')


class EditCommentForm(Form, ErrorForm):
    content = forms.CharField()
    comment_id = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        self.comment = kwargs.pop('comment', None)
        super(EditCommentForm, self).__init__(*args, **kwargs)

    def clean(self):
        if not self.comment.exists():
            raise forms.ValidationError('Not allowed!')
        comment = self.comment.get()
        if self.cleaned_data.get('content') == comment.content:
            raise forms.ValidationError('Enter new value!')

        self.cleaned_data['comment'] = comment
        return self.cleaned_data


class DeleteCommentForm(ModelForm, ErrorForm):
    class Meta:
        model = Comment
        fields = ('id',)

    id = forms.IntegerField(required=True)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(DeleteCommentForm, self).__init__(*args, **kwargs)

    def clean(self):
        comment = Comment.objects.filter(pk=self.cleaned_data.get('id'), user=self.user)
        if not comment.exists():
            raise forms.ValidationError('Not allowed!')
        else:
            self.cleaned_data['comment'] = comment

        return self.cleaned_data


class ArticleLikeForm(ModelForm, ErrorForm):
    class Meta:
        model = Like
        fields = ('article',)


class CommentLikeForm(ModelForm, ErrorForm):
    class Meta:
        model = Like
        fields = ('comment',)
