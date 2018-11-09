from django import forms
from .models import ArticleColumn


class ArtileColumnForm(forms.ModelForm):
    class Meta:
        model = ArticleColumn
        fields = ('column',)
