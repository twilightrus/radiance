from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from django.urls import reverse

from .models import Article

from django.views.generic import ListView, DetailView


class ArticleListView(ListView):

    queryset = Article.objects.order_by('-pub_date')
    template_name = 'blog/index.html'
    context_object_name = 'articles'


class ArticleDetailView(DetailView):

    model = Article
    template_name = 'blog/detail.html'
    context_object_name = 'article'
