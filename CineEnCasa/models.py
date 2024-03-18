from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User

# SUPERUSER: admin | admin@admin.com | 1234

# Revert all migrations:
# python manage.py migrate CineEnCasa zero
# python manage.py makemigrations CineEnCasa
# python manage.py migrate CineEnCasa

# Choices
MONTH_CHOICE = [
    ("JAN", "January"), ("FEB", "February"), ("MAR", "March"), ("APR", "April"), ("MAY", "May"), ("JUN", "June"),
    ("JUL", "July"), ("AUG", "August"), ("SEP", "September"), ("OCT", "October"), ("NOV", "November"),
    ("DEC", "December")
]


class Platform(models.Model):
    name = models.CharField(max_length=20, unique=True)
    color = models.CharField(max_length=7, default="#000000")

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=30, unique=True)
    flag = models.ImageField(upload_to="media/country-flags", default="media/country-flags/default.png")

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class LanguageVersion(models.Model):
    name = models.CharField(max_length=4, unique=True, blank=True)

    def __str__(self):
        return self.name


class FilmType(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Saga(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=True)
    total_films = models.PositiveIntegerField(default=2)

    def __str__(self):
        return self.name


class Film(models.Model):
    # Movie info
    title = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField()
    duration = models.DurationField()  # HH:MM -> forms.py
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    synopsis = models.TextField()
    poster = models.ImageField(upload_to="media/film-posters", default="media/film-posters/default.png")

    # Extra info
    type = models.ForeignKey(FilmType, on_delete=models.CASCADE)
    language_version = models.ManyToManyField(LanguageVersion)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    # Saga equals series/tv shows (episodes), sagas (movies), tv program (gala)
    saga = models.ForeignKey(Saga, on_delete=models.SET_NULL, null=True, blank=True)
    current_saga_film = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


class Billboard(models.Model):
    week = models.AutoField(primary_key=True)
    films = models.ManyToManyField(Film, blank=True)


class BillboardFilm(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

    # Date info
    hour = models.TimeField(default='20:00')
    day = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(31)])
    month = models.CharField(choices=MONTH_CHOICE, max_length=10)


class Review(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    comment = models.TextField()
