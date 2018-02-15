from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from django.urls import reverse

from .models import Article


@login_required(redirect_field_name=None)
def index(request):
    articles = Article.objects.order_by("-pub_date")
    context = {'title': 'Blog',
               'articles': articles}
    return render(request, "blog/index.html", context)


@login_required(redirect_field_name=None)
def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {'previous': article.get_previous_id(), 'next': article.get_next_id(),
               'article': article}
    return render(request, 'blog/detail.html', context)
