from django import forms
from .models import ArticleColumn, ArticlePost, ArticleTag


class ArtileColumnForm(forms.ModelForm):
    class Meta:
        model = ArticleColumn
        fields = ('column',)


class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = ArticlePost
        fields = ('title', 'body')


class ArticleTagForm(forms.ModelForm):
    class Meta:
        model = ArticleTag
        fields = ('tag',)
