from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class BlogArticles(models.Model):
    title = models.CharField(max_length=300, verbose_name='文章标题')
    # Django2.0中外键和一对一关系时要加on_delete选项，选择CASCADE是级联删除
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name='作者')
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now, verbose_name='发布时间')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
