"""
URL configuration for Cine_En_Casa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CineEnCasa.views import home, add_film, film_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('films/add/', add_film, name='add_film'),
    path('films/<str:title>/', film_detail, name='film_detail'),
]