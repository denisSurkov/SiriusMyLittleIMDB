from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import FilmModel, FilmGenre, ProductionCountry
from .api.serializers import FilmSerializer, GenreSerializer, CountrySerializer
from .filters import FilmDateFilter


def main_view(request):
    return render(request, 'main_page.html')


class FilmViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FilmModel.objects.all()
    serializer_class = FilmSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, )
    filterset_class = FilmDateFilter

    search_fields = ('title', )

    filter_fields = ('release_date', 'genres', 'production_countries', )


class GenresViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FilmGenre.objects.all()
    serializer_class = GenreSerializer


class CountriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductionCountry.objects.all()
    serializer_class = CountrySerializer
