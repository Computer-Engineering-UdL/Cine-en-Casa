from django.contrib import admin
from CineEnCasa.models import Film, Platform, Country, Genre, LanguageVersion


# Register your models here.

class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year')
    search_fields = ('title', 'release_year')


admin.site.register(Film, FilmAdmin)
admin.site.register(Platform)
admin.site.register(Country)
admin.site.register(Genre)
admin.site.register(LanguageVersion)