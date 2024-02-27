from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from blog.models import Category, Article


# Create your views here.
@login_required(login_url='login')
def list_articles(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 2)
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)
    return render(request, 'articles/list.html', {
        'title': 'Artículos',
        'articles': page_articles
    })


@login_required(login_url='login')
def get_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    # articles = Article.objects.filter(categories=category)
    return render(request, 'categories/category.html', {
        'title': category.name,
        'category': category,
        # 'articles': articles
    })


@login_required(login_url='login')
def get_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/detail_article.html', {'article': article})
