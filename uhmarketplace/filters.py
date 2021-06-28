import django_filters
from .models import Textbook


class TextbookFilter(django_filters.FilterSet):
    class Meta:
        model = Textbook
        fields = {
            'book_title': ['icontains'],
            'book_author': ['icontains'],
            'content': ['icontains'],
            'course': ['icontains'],
        }