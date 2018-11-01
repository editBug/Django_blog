from django.shortcuts import render, get_object_or_404
from .models import BlogArticles


# Create your views here.

def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, 'blog/titles.html', {'blogs': blogs})

def blog_article(request, article_id):
    # article = BlogArticles.objects.get(id=article_id)
    # 在顶部引入get_object_or_404，当页面找不到时，显示404错误
    article = get_object_or_404(BlogArticles, id=article_id)
    pub = article.publish
    return render(request, 'blog/content.html', {'article': article, 'publish': pub})