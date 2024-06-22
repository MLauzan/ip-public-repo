# capa de vista/presentación
# si se necesita algún dato (lista, valor, etc), esta capa SIEMPRE se comunica con services_nasa_image_gallery.py

from django.shortcuts import redirect, render
from .layers.services import services_nasa_image_gallery
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .layers.generic.utils import *

# función que invoca al template del índice de la aplicación.
def index_page(request):
    return render(request, 'index.html')

def login_page(request):
        return render(request, 'registration/login.html')

# auxiliar: retorna 2 listados -> uno de las imágenes de la API y otro de los favoritos del usuario.
def getAllImagesAndFavouriteList(request, input, page):
    fetchImages = services_nasa_image_gallery.getAllImages(input, page)
    images = fetchImages[0]
    pages  = fetchImages[1]
    favourites = services_nasa_image_gallery.getAllFavouritesByUser(request)
    favourite_list = favourites

    return images, favourite_list, pages

# función principal de la galería.
def home(request):
    page = request.GET.get('page') or '1'
    fetchImagesAndFavourites = getAllImagesAndFavouriteList(request, input=None, page=page)
    
    images = fetchImagesAndFavourites[0]
    favourite_list = fetchImagesAndFavourites[1]

    pages = int(fetchImagesAndFavourites[2])
    previous_pages= getPreviousPages(int(page))
    next_pages = getNextPages(int(page), pages)

    return render(request, 'home.html', {'images': images, 'favourite_list': favourite_list, 'query': 'space', 'pages': pages, 'previous_pages' : previous_pages, 'next_pages' : next_pages} )


# función utilizada en el buscador.
def search(request):
    search_msg = request.GET.get('query') or 'space'
    page = request.GET.get('page') or '1'

    images, favourite_list, pages = getAllImagesAndFavouriteList(request, search_msg, page)

    if not images:
        return render(request, 'home.html', {'error': 'No se encontraron imágenes para '} )

    previous_pages= getPreviousPages(int(page))
    next_pages = getNextPages(int(page), pages)    

    return render(request, 'home.html', {'images': images, 'favourite_list': favourite_list, 'query': search_msg, 'pages': str(pages), 'previous_pages' : previous_pages, 'next_pages' : next_pages} )


# las siguientes funciones se utilizan para implementar la sección de favoritos: traer los favoritos de un usuario, guardarlos, eliminarlos y desloguearse de la app.
@login_required
def getAllFavouritesByUser(request):
    favourite_list =  services_nasa_image_gallery.getAllFavouritesByUser(request)
    return render(request, 'favourites.html', {'favourite_list': favourite_list})


@login_required
def saveFavourite(request):
    services_nasa_image_gallery.saveFavourite(request)
    return redirect('home')


@login_required
def deleteFavourite(request):
    services_nasa_image_gallery.deleteFavourite(request)
    return redirect('favoritos')

@login_required
def exit(request):
    logout(request)
    return redirect('home')