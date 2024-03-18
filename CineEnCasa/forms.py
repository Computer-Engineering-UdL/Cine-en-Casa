from django import forms
from CineEnCasa.models import Film


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ('title', 'release_year', 'duration', 'country', 'synopsis', 'poster', 'type', 'platform')