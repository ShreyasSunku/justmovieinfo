from django.db import models

# Create your models here.


class Movies(models.Model):
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    movie_id = models.CharField(max_length=70, unique=True)
    # dummy = models.CharField(max_length=20, default=None)
    class Meta:
        db_table = 'movies'


class Movie_Info(models.Model):
    movie_info = models.TextField()
    image_name = models.CharField(max_length=200)
    movie = models.OneToOneField(Movies, on_delete=models.CASCADE, related_name='movie', db_column='movie_id', to_field='movie_id')

    class Meta:
        db_table = 'movie_info'


class Movie_Verdict(models.Model):
    verdict_link = models.CharField(max_length=500)
    comment = models.TextField()
    rating = models.CharField(max_length=10)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='movie_verdict', db_column='movie_id', to_field='movie_id')
    class Meta:
        db_table = 'movie_verdict_info'


class LoginForm(models.Model):
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=10)
    mail = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)

class Purchase(models.Model):
    purcased = models.IntegerField()
    user = models.IntegerField()