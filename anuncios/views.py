from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # TODO logica da view
    return HttpResponse("Olá mundo")
