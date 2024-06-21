from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description=models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    release_date=models.DateTimeField()
    actors=models.CharField(max_length=200)
    movie_logo = models.FileField()
    youtube_link=models.URLField()

    def __str__(self):
        return self.title


class Myrating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])

class MyList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watch = models.BooleanField(default=False)