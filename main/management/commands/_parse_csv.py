import csv
import logging
from collections import namedtuple
from datetime import datetime
import os.path
import ast

logging.basicConfig(level=logging.WARNING)
TITLE_ROW = 'adult,belongs_to_collection,budget,genres,homepage,id,imdb_id,original_language,original_title,overview,popularity,poster_path,production_companies,production_countries,release_date,revenue,runtime,spoken_languages,status,tagline,title,video,vote_average,vote_count'
FilmData = namedtuple('FilmData', TITLE_ROW.split(','))

FILENAME = os.path.normpath(os.path.join(__file__,'..', 'movies_metadata.csv'))


def get_films_from_csv():

    for film_row in load_data_from_file():
        new_film = parse_film_row(film_row)
        logging.debug('load new film')
        yield new_film


def parse_film_row(film_row: list) -> FilmData:
    film_data = FilmData(
        film_row[0] == "True",
        film_row[1],
        float(film_row[2] or 0),
        ast.literal_eval(film_row[3]),
        film_row[4],
        int(film_row[5]),
        film_row[6],
        film_row[7],
        film_row[8],
        str(film_row[9]),
        float(film_row[10]),
        film_row[11],
        film_row[12],
        ast.literal_eval(film_row[13]),
        datetime.strptime(film_row[14] or '1000-01-01', '%Y-%m-%d'),
        float(film_row[15] or 0),
        float(film_row[16] or 0),
        film_row[17],
        film_row[18],
        film_row[19],
        film_row[20],
        film_row[21] == 'True',
        float(film_row[22] or 0),
        float(film_row[23] or 0)
    )
    return film_data


def load_data_from_file(filename=FILENAME):

    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)

        next(reader)  # to avoid title line

        for r in reader:
            if len(r) >= 23: yield r



if __name__ == '__main__':
    get_films_from_csv()