from datetime import date

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from CineEnCasa.forms import FilmForm, BillboardForm, BillboardFilmForm
from django.contrib import messages
from CineEnCasa.models import Film, BillboardFilm, Billboard


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





def create_new_billboard(request):
    if request.method == 'POST':
        form = BillboardFilmForm(request.POST)
        if form.is_valid():
            billboardFilm = form.save()
            billboard = Billboard()
            billboard.save()
            billboard.films.add(billboardFilm)
            billboard.save()
            #return HttpResponseRedirect(reverse("create_current_billboard", args=(billboard.week,)))
            return redirect('create_current_billboard', pk=billboard.pk)
            #return render(request, 'create_current_billboard.html', {'billboard': billboard})
    else:
        form = BillboardFilmForm()
    return render(request, 'create_new_billboard.html', {'form': form})

def create_current_billboard(request, pk):
    billboard = get_object_or_404(Billboard, pk=pk)

    if request.method == 'POST':
        form = BillboardFilmForm(request.POST)
        if form.is_valid():
            billboardFilm = form.save()
            billboard.films.add(billboardFilm)
            billboard.save()
            films = BillboardFilm.objects.all()
            print(billboard.pk)
            #return redirect('create_current_billboard', pk=billboard.pk, billboard=billboard)
            return render(request, 'create_current_billboard.html', {'form': form, 'billboard': billboard})
    else:
        form = BillboardFilmForm()
    return render(request, 'create_current_billboard.html', {'form': form, 'billboard': billboard})





def list_films(request):
    films = Film.objects.all()

    search_query = request.GET.get('search')
    if search_query:
        films = films.filter(title__icontains=search_query)

    order_by = request.GET.get('order_by')
    if order_by:
        films = films.order_by(order_by)

    return render(request, 'list_films.html', {'films': films})
