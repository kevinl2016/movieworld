import kronos

from movie.models import Movie
from movie.clients import ApiClient

movie_client = ApiClient()
FIEL_DATA_MAPPING = (
    ('title', 'Title', None),
    ('year','Year', None),
    ('released','Released', None),
    ('runtime','Runtie', None),
    ('genre','Genre', None),
    ('director','Director', None),
    ('writer','Writer', None),
    ('actors','Actors', None),
    ('plot','Plot', None),
    ('language','Language', None),
    ('poster','Poster', None),
    ('meta_score','Metascore', None),
    ('rating','Rating', lambda x: float(x.replace(',', ''))),
    ('votes','Votes', lambda x: float(x.replace(',', ''))),
    ('movie_id','ID', None),
    ('media_type','Type', None),
    ('price', 'Price', lambda x: float(x.replace(',', ''))),
    ('country','Country', None)
)

def _transform_with_default(value, transform_function, default=None):
    if transform_function:
        if default:
            return transform_function(value,default=default)
        return transform_function(value)
    return value

@kronos.register('0 */6 * * *')
def craw_movies():
    source = [
        'filmworld',
        'movieworld'
    ]
    for site in source:
        response =  movie_client.request(api_path='{}/movies'.format(site))
        print(response.status_code)
        if response.status_code == 200:
            movies = response.json().get('Movies')
            for movie in movies:
                update_insert_movie(api_path='{}/movie/{}'.format(site, movie.get('ID')))

def update_insert_movie(api_path):
    print(api_path)
    response = movie_client.request(api_path=api_path)
    if response.status_code == 200:
        movie = response.json()
        movie_id = movie.get('ID')
        defalut_data = {}
        for key_to, key_from, transform_value in FIEL_DATA_MAPPING:
            value = movie.get(key_from)
            if value:
                defalut_data[key_to] = _transform_with_default(
                    value,
                    transform_value
                )
        print(defalut_data)
        obj, _ = Movie.objects.update_or_create(movie_id=movie_id,
            defaults = defalut_data
        )
