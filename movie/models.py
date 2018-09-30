from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255, blank=True)
    year = models.IntegerField(default=1900)
    released = models.CharField(max_length=20, blank=True)
    runtime = models.CharField(max_length=30, blank=True)
    genre = models.CharField(max_length=255, blank=True)
    director = models.CharField(max_length=60, blank=True)
    writer = models.CharField(max_length=60, blank=True)
    actors = models.TextField(blank=True)
    plot = models.TextField(blank=True)
    language = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=30, blank=True)
    poster = models.URLField(blank=True)
    meta_score = models.FloatField(default=0)
    rating = models.FloatField(default=0)
    votes = models.FloatField(default=0)
    movie_id = models.CharField(max_length=10, blank=True)
    media_type = models.CharField(max_length=10, blank=True)
    media_source = models.CharField(max_length=10, blank=True)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.title