from main.models import FilmModel, FilmGenre, ProductionCountry
from rest_framework import serializers


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmModel
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmGenre
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionCountry
        fields = '__all__'
