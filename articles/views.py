from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm


# Create your views here.
def article_list(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/home_view.html', context)


def article_search_view(request):
    query_dict = request.GET
    try:
        query = int(query_dict.get('q'))
    except:
        query = None
    article = None
    if query is not None:
        article = Article.objects.get(pk=query)
    context = {
        'article': article
    }
    return render(request, 'articles/article_search.html', context)


def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/article_detials.html', context)


@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        article_obj = form.save()
        context['form'] = ArticleForm()
        # context['object'] = article_obj
        # context['is_created'] = True

    return render(request, 'articles/create_article.html', context)
