from functools import lru_cache
from django.core.management.base import BaseCommand
from main.models import FilmModel, FilmGenre, ProductionCountry

from ._parse_csv import get_films_from_csv, TITLE_ROW

TITLE_ROW_LIST = TITLE_ROW.split(',')


class Command(BaseCommand):
    help = 'Uploads films to DB from movies_metadata.csv'

    def handle(self, *args, **options):

        for film in get_films_from_csv():
            c_dict = self._parse_film(film)
            genres = c_dict['genres']
            countries = c_dict['production_countries']

            del c_dict['genres'], c_dict['production_countries']


            obj, created = FilmModel.objects.get_or_create(**c_dict)

            for i in genres: obj.genres.add(i)
            for i in countries: obj.production_countries.add(i)

            if created:
                self.stdout.write(self.style.SUCCESS('Successfully created new film: %s' % obj.title))
            else:
                self.stdout.write(self.style.SUCCESS('Film %s already in base' % obj.title))

        self.stdout.write(self.style.SUCCESS('Successfully uploaded all films'))


    def _parse_film(self, film_data) -> dict:
        current_dict = {}
        counter = 0

        for i in TITLE_ROW_LIST:
            current_dict[i] = film_data[counter]
            counter += 1

        del current_dict['id']

        current_dict['production_countries'] = list(map(lambda c: _get_production_country_by_name(c['name'])[0],
                                                        current_dict['production_countries']))
        current_dict['genres'] = list(map(lambda g: _get_genre_by_name(g['name'])[0], current_dict['genres']))

        return current_dict


def _get_genre_by_name( genre_name):
    return FilmGenre.objects.get_or_create(name=genre_name)


def _get_production_country_by_name(country_name):
    return ProductionCountry.objects.get_or_create(name=country_name)