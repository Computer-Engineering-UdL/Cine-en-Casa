from django.contrib import admin
from CineEnCasa.models import Film, Platform, Country, Genre, LanguageVersion, FilmType, Saga
from CineEnCasa.models import Billboard, BillboardFilm


# Register your models here.

class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'release_year', 'duration', 'platform', 'saga')
    search_fields = ('title', 'country', 'release_year', 'duration', 'platform', 'saga')


admin.site.register(Film, FilmAdmin)
admin.site.register(Platform)
admin.site.register(Country)
admin.site.register(Genre)
admin.site.register(LanguageVersion)
admin.site.register(FilmType)
admin.site.register(Saga)
admin.site.register(Billboard)
admin.site.register(BillboardFilm)
