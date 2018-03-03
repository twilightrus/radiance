from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import View, ListView, DetailView, FormView, CreateView
from django.http import JsonResponse, Http404, HttpResponse
from django.core import serializers
from django.db.models import Case, When, BooleanField, Q, Count

from .models import *
from .forms import *


class AjaxableResponseMixin:

    def response(self, data={'status': 'ok'}):
        return JsonResponse(data)

    def error_response(self, data={'status': 'error'}):
        return JsonResponse(data, status=400)


class AjaxableFormResponseMixin(AjaxableResponseMixin):
    """
        Mixin to add AJAX support to a form.
        Must be used with an object-based FormView (e.g. CreateView)
        """

    def form_invalid(self, form):
        if self.request.is_ajax():
            return super().response(form.errors)
        else:
            raise Http404()

    def form_valid(self, form):
        if self.request.is_ajax():
            return super().response()
        else:
            raise Http404()


class ArticleListView(ListView):

    template_name = 'blog/index.html'
    context_object_name = 'articles'
    paginate_by = 6

    def get_queryset(self):
        articles = Article.objects.order_by('-pub_date')
        #articles = Article.objects.order_by('-pub_date').annotate(
        #    is_liked=Case(
        #        When(like__user_id_id=self.request.user.id, then=True),
        #        default=False,
        #        output_field=BooleanField()
        #    )
        #)
        #articles = Article.objects.order_by('-pub_date')
        #id_articles = [q.id for q in articles]
        #is_liked_list = Article.objects.annotate(
        #    is_liked=Case(
        #        When(Q(like__article_id_id__in=id_articles) & Q(like__user_id_id=self.request.user.id), then=True),
        #        default=False,
        #        output_field=BooleanField()
        #    ))
        return articles


class ArticleDetailView(DetailView):

    model = Article
    template_name = 'blog/detail.html'
    context_object_name = 'article'


class CommentsView(AjaxableResponseMixin, View):

    def get_object(self, queryset=None):
        return Comment.objects.filter(article=self.kwargs['pk']).order_by('-pub_date')

    def get(self, request, *args, **kwargs):

        return super().response(self.get_data())

    def get_data(self):
        comments = {}
        i = 0
        obj = self.get_object()
        for comment in obj:
            comments[i] = comment.as_dict(self.request)
            i = i + 1
        return {'status': 'ok',
                'comments': comments,
                'comments_count': obj.count()}


class LikesView(AjaxableResponseMixin, View):

    def get_object(self, queryset=None):
        count_likes = Article.objects.get(pk=self.kwargs['pk']).like_set.count()
        is_liked = Like.objects.filter(article=self.kwargs['pk'], user=self.request.user).exists()
        return {'count_likes': count_likes,
                'is_liked': is_liked}

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        data = {'status': 'ok',
                'count_likes': obj["count_likes"],
                'is_liked': obj["is_liked"]}
        return super().response(data)


class CommentCreateView(AjaxableFormResponseMixin, CreateView):

    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(CommentCreateView, self).form_valid(form)


class ArticleLikeCreateView(AjaxableFormResponseMixin, CreateView):

    model = Like
    form_class = ArticleLikeForm

    def form_valid(self, form):
        like = Like.objects.filter(article=form.cleaned_data.get('article'), user=self.request.user)

        if like.exists():
            like.delete()

        else:
            Like(article=form.cleaned_data.get('article'), user=self.request.user).save()

        return super(ArticleLikeCreateView, self).form_valid(form)


class CommentLikeCreateView(AjaxableFormResponseMixin, CreateView):

    model = Like
    form_class = CommentLikeForm

    def form_valid(self, form):
        like = Like.objects.filter(comment=form.cleaned_data.get('comment'), user=self.request.user)

        if like.exists():
            like.delete()

        else:
            Like(comment=form.cleaned_data.get('comment'), user=self.request.user).save()

        return super(CommentLikeCreateView, self).form_valid(form)
