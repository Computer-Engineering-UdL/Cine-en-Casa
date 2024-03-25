from django.shortcuts import render, redirect, get_object_or_404
from CineEnCasa.forms import FilmForm, BillboardForm, BillboardFilmForm
from django.contrib import messages
from CineEnCasa.models import Film
from .models import Billboard


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
    return render(request, 'film_detail.html', {'film': film})


def create_billboard(request):
    if request.method == 'POST':
        form = BillboardFilmForm(request.POST)
        if form.is_valid():
            billboardFilm = form.save()
            films = Billboard.objects.all()
            messages.success(request, 'ole tus cojones')
            return render(request, 'create_billboard.html', {'films': films})
    else:
        form = BillboardFilmForm()
        messages.error(request, 'mongolo')
    return render(request, 'create_billboard.html', {'form': form})


def list_films(request):
    films = Film.objects.all()

    search_query = request.GET.get('search')
    if search_query:
        films = films.filter(title__icontains=search_query)

    order_by = request.GET.get('order_by')
    if order_by:
        films = films.order_by(order_by)

    return render(request, 'list_films.html', {'films': films})
