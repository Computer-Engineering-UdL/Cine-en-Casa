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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from CineEnCasa.views import home, add_film, film_detail, create_new_billboard, create_current_billboard
from django.conf.urls.static import static
from CineEnCasa import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('films/add/', add_film, name='add_film'),
    path('billboard/create/', create_new_billboard, name='create_new_billboard'),
    path('billboard/create/<int:pk>', create_current_billboard, name='create_current_billboard'),
    path('films/<str:title>/', film_detail, name='film_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)