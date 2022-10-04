from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):  # Nome do método poderia ser qualquer um. Index é convenção. O nome request também é convenção. Toda vida é feito um request ao abrir a página.
    return HttpResponse("Olá mundo!")