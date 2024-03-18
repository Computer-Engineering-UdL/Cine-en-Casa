from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User

# SUPERUSER: admin | admin@admin.com | 1234

# Revert all migrations:
# python manage.py migrate CineEnCasa zero
# python manage.py makemigrations CineEnCasa
# python manage.py migrate CineEnCasa

# Choices
LANGUAGE_CHOICES = [
    ('VOSE', 'VOSE'),
    ('VE', 'VE')
]

MONTH_CHOICE = [
    ("JAN", "Enero"),
    ("FEB", "Febrero"),
    ("MAR", "Marzo"),
    ("APR", "Abril"),
    ("MAY", "Mayo"),
    ("JUN", "Junio"),
    ("JUL", "Julio"),
    ("AUG", "Agosto"),
    ("SEP", "Septiembre"),
    ("OCT", "Octubre"),
    ("NOV", "Noviembre"),
    ("DEC", "Diciembre")
]

TYPE_CHOICE = [
    ("SAGA", "SAGA"),
    ("MOVIE", "PELÍCULA"),
    ("DOCU-SERIES", "DOCU-SERIE"),
    ("EVENT", "EVENTO"),
    ("TV_SHOW", "SERIE"),
    ("TV_PROGRAM", "PROGRAMA"),
    ("DOCUMENTARY", "DOCUMENTAL"),
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


class Film(models.Model):
    # Movie info
    title = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField()
    duration = models.TimeField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    synopsis = models.TextField()
    poster = models.ImageField()

    # Extra info
    type = models.CharField(choices=TYPE_CHOICE, max_length=15)
    # language_versions = models.ManyToManyField(LANGUAGE_CHOICES, maxlength=5, blank=True)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    is_saga = models.BooleanField()  # Saga equals series/tv shows (episodes), sagas (movies), tv program (gala)

    # If is_saga:
    total_films = models.PositiveIntegerField(default='3')
    current_film = models.PositiveIntegerField(default='1')
    saga_type = models.CharField(max_length=4)

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
