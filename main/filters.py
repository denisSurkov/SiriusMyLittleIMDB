from django_filters import DateFromToRangeFilter, FilterSet
from main.models import FilmModel


class FilmDateFilter(FilterSet):
    release_date = DateFromToRangeFilter('release_date')

    class Meta:
        model = FilmModel
        fields = ['release_date', 'genres', 'production_countries']

