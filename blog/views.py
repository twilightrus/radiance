from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView, CreateView

from .models import Article


class ArticleListView(ListView):

    queryset = Article.objects.order_by('-pub_date')
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    paginate_by = 6


class ArticleDetailView(DetailView):

    model = Article
    template_name = 'blog/detail.html'
    context_object_name = 'article'
