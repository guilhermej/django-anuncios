from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from .models import Categoria
from .models import Anuncio


def home(request):
    categorias = Categoria.objects.all()

    ultimos_anuncios = Anuncio.objects.all()[:12]

    return render(request, 'home.html', {'categorias': categorias,
                                         'anuncios': ultimos_anuncios})


def categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    categorias = Categoria.objects.all()

    anuncios = Anuncio.objects.filter(categoria=categoria)

    return render(request, 'home.html', {'categorias': categorias,
                                         'anuncios': anuncios,
                                         'categoria': categoria})


def anuncio(request, anuncio_id):
    anuncio = get_object_or_404(Anuncio, id=anuncio_id)

    categorias = Categoria.objects.all()

    return render(request, 'anuncio.html', {'categorias': categorias,
                                         'anuncio': anuncio})
