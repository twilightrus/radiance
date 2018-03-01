from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView, FormView, CreateView
from django.http import JsonResponse, Http404
from django.core import serializers

from .models import Article
from .forms import *


class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            raise Http404()

    def form_valid(self, form):
        if self.request.is_ajax():
            return JsonResponse(self.data)
        else:
            raise Http404()


class ArticleListView(ListView):

    queryset = Article.objects.order_by('-pub_date')
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    paginate_by = 6


class ArticleDetailView(DetailView):

    model = Article
    template_name = 'blog/detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['comments'] = self.object.comment_set.all().order_by('-pub_date')
        return context


class CommentCreate(AjaxableResponseMixin, CreateView):

    model = Comment
    form_class = CommentForm

    def get_data(self):
        comments = {}
        qs = Comment.objects.filter(article_id=self.request.POST["article_id"]).order_by('-pub_date')
        i = 0
        for comment in qs:
            comments[i] = comment.as_dict()
            i = i + 1
        return {'status': 'ok',
                'comments': comments,
                'comments_count': qs.count()}

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        form.save()
        article = Article.objects.get(pk=self.request.POST["article_id"])
        article.count_comments += 1
        article.save()
        self.data = self.get_data()
        return super(CommentCreate, self).form_valid(form)
