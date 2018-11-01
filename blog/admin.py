from django.contrib import admin
from .models import BlogArticles


# Register your models here.
# admin.sites.register(BlogArticles)

class BlogArticlesAdmin(admin.ModelAdmin):
    # 文章导航栏显示的内容
    list_display = ("title", "author", "publish")
    # 右侧过滤器，以发布时间和作者排序
    list_filter = ("publish", "author")
    # 顶部搜索框
    search_fields = ('title', "body")
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ['-publish', 'author']


admin.site.register(BlogArticles, BlogArticlesAdmin)
