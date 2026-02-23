from django.shortcuts import render
from .models import Article

from django.views.generic import (
    ListView
)

# Create your views here.
def list_articles(request):
    articles = Article.objects.all()

    context = {
        'articles': articles
    }

    return render(request, 'article_list.html', context)

def details_article(request, article_id):
    article = Article.objects.get(id = article_id)

    context = {
        'article': article
    }

    return render(request, 'article_details.html', context)

class ClassBasedView(ListView):
    template_name="article_list.html"
    queryset = Article.objects.all()