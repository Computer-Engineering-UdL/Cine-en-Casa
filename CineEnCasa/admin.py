from django.contrib import admin
from .models import Film


# Register your models here.

class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year')
    search_fields = ('title', 'release_year')


admin.site.register(Film, FilmAdmin)
