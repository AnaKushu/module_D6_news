import django_filters
from django.forms import DateInput
from django_filters import FilterSet, DateFilter
from django.utils.translation import gettext_lazy as _
from .models import Post, Category


class PostFilter(FilterSet):
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label=_('Название'),
    )

    postCategory = django_filters.ModelChoiceFilter(
        field_name='postCategory',
        queryset=Category.objects.all(),
        label=_('Категория'),
        empty_label=_('Выберите категорию')
    )

    data = DateFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        widget=DateInput(
            format='%Y-%m-%dT',
            attrs={'type': 'date'},
        ),
        label=_('Дата публикации')
    )


    class Meta:
        model = Post
        fields = {
            'title',
            'postCategory',
        }