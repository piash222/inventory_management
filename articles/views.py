from django.shortcuts import render
from .models import Article


# Create your views here.
def article_list(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/home_view.html', context)


def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/article_detials.html', context)
