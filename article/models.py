from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from slugify import slugify


# Create your models here.

class ArticleColumn(models.Model):
    user = models.ForeignKey(User, related_name='article_column', on_delete=models.CASCADE)
    column = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.column


class ArticleTag(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tag')
    tag = models.CharField(max_length=500)

    def __str__(self):
        return self.tag


class ArticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500)
    column = models.ForeignKey(ArticleColumn, on_delete=models.CASCADE, related_name='article_column')
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    users_like = models.ManyToManyField(User, related_name='articles_like', blank=True)
    article_tag = models.ManyToManyField(ArticleTag, related_name='article_tag', blank=True)

    class Meta:
        ordering = ('-updated',)
        # 建立索引，提高读取速度
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

    # 重写save方法，用于实现中文title转拼音存储，以备后期在浏览器url上显示
    def save(self, *args, **kargs):
        self.slug = slugify(self.title)
        super(ArticlePost, self).save(*args, **kargs)

    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.id, self.slug])

    def get_url_path(self):
        return reverse('article:list_article_detail', args=[self.id, self.slug])
