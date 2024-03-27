from django import forms
from CineEnCasa.models import Film, Billboard, BillboardFilm


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = (
            'title', 'release_year', 'duration', 'country', 'genre', 'synopsis', 'poster',
            'type', 'language_version', 'platform', 'saga',
        )


class BillboardForm(forms.ModelForm):
    class Meta:
        model = Billboard
        fields = ('week', 'films')


class BillboardFilmForm(forms.ModelForm):
    class Meta:
        model = BillboardFilm
        fields = ('film', 'datetime', 'current_saga_film')
