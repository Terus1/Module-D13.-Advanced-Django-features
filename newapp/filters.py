from django_filters import FilterSet, ModelChoiceFilter, DateTimeFilter
from .models import Post, Category
from django.forms import DateTimeInput


class PostFilter(FilterSet):
    category = ModelChoiceFilter(
        field_name='category__name_category',
        queryset=Category.objects.all(),
        label='Категория',
        empty_label='Все категории'
    )
    time_in = DateTimeFilter(
        field_name='time_in',
        lookup_expr='gt',
        label='Дата',
        widget=DateTimeInput(
            # format='%m/%d/%Y %H:%M',
            # attrs={'type': 'datetime-local'},
            format='%Y/%m/%dT %H:%M',
            attrs={'type': 'datetime-local'},
        )
    )

    class Meta:

        model = Post
        fields = {
            'title': ['icontains']
        }
