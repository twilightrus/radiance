from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView

from .models import Article


class ArticleListView(ListView):

    queryset = Article.objects.order_by('-pub_date')
    template_name = 'blog/index.html'
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        paginator = Paginator(context['articles'], 6)
        page = self.kwargs.get('page')
        context['articles'] = paginator.get_page(page)
        return context


class ArticleDetailView(DetailView):

    model = Article
    template_name = 'blog/detail.html'
    context_object_name = 'article'
