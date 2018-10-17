from django.db import models
from django.contrib.postgres.fields import JSONField


class FilmGenre(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'genre'
        verbose_name_plural = 'genres'


class ProductionCountry(models.Model):
    name = models.CharField(max_length=512)

    class Meta:
        verbose_name = 'production country'
        verbose_name_plural = 'production countries'
        ordering = ('name', )

class FilmModel(models.Model):
    adult = models.NullBooleanField()
    belongs_to_collection = JSONField(null=True)
    budget = models.IntegerField(null=True)
    homepage = models.URLField(null=True, max_length=1024)

    imdb_id = models.CharField(max_length=254, null=True)

    original_language = models.CharField(max_length=254, null=True)
    original_title = models.TextField(null=True)

    overview = models.TextField(null=True)
    popularity = models.FloatField(null=True)
    poster_path = models.URLField(null=True)
    production_companies = JSONField(null=True)
    release_date = models.DateField(null=True)
    runtime = models.FloatField(null=True)
    spoken_languages = JSONField(null=True)

    genres = models.ManyToManyField(FilmGenre)
    production_countries = models.ManyToManyField(ProductionCountry)

    revenue = models.FloatField(null=True)

    status = models.CharField(max_length=254, null=True)
    tagline = models.TextField(null=True)
    title = models.TextField(null=True)
    video = models.NullBooleanField(null=True)

    vote_average = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)