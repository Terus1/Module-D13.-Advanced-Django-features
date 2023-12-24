from django import forms
from .models import Post


class NewForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            #'categoryType',
            'category',
            'title',
            'text_post',
            'rating_post',
        ]


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            #'categoryType',
            'category',
            'title',
            'text_post',
            'rating_post',
        ]
