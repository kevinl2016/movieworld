from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^(?P<movie_id>[0-9a-zA-Z]+[0-9])$', views.movie, name='movie'),
    url(r'^search$', views.search, name='search'),
]