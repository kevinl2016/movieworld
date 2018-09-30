from django.shortcuts import render, render_to_response
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

from movie.models import Movie


def index(request):
    top_fives = Movie.objects.all()#.order_by(-rating)[:5]
    context = {
        'movies': top_fives
    }
    return render(request, 'movie/home.html', context)
# Create your views here.

def movie(request, movie_id):
    movie = Movie.objects.get(movie_id=movie_id)
    context = {
        'item': movie
    }
    return render(request, 'movie/details.html', context)

@csrf_exempt
def search(request):
    print('111')
    key_word = request.POST.get('key_word')
    sort = request.POST.get('sort')
    if sort is None:
        sort = 'price'

    if sort != 'price':
        sort = '-' + sort 
    if not key_word:
         movies = Movie.objects.all().order_by(sort)
    else:
        movies = Movie.objects.filter(Q(title__contains=key_word)|Q(actors__contains=key_word)).order_by(sort)
    
    context = {
        'movies': movies,
        'hidden_key': key_word
    }
    if request.is_ajax():
        return render(request, 'movie/movie_list.html', context)
    else:
        return render(request, 'movie/home.html', context)
