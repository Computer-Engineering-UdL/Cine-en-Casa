from django.shortcuts import render, redirect, get_object_or_404
from CineEnCasa.forms import FilmForm, BillboardForm
from CineEnCasa.models import Film


# Create your views here.

def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            film = form.save()
            return redirect('home')
    else:
        form = FilmForm()
    return render(request, 'add_film.html', {'form': form})


def home(request):
    films = Film.objects.all()
    return render(request, 'home.html', {'films': films})


def film_detail(request, title):
    film = get_object_or_404(Film, title=title)
    genres = film.genre.all()
    return render(request, 'film_detail.html', {'film': film, 'genres': genres})


def create_billboard(request):
    if request.method == 'POST':
        form = BillboardForm(request.POST)
        if form.is_valid():
            billboard = form.save()
            return redirect('home')
    else:
        form = BillboardForm()
    return render(request, 'create_billboard.html', {'form': form})