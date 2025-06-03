from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def autor(request):
    saludar = "Hola, soy el autor de este blog"
    return HttpResponse(saludar)

def posteo(request):
    saludar = "Hola, soy un posteo de este blog"
    return HttpResponse(saludar)

def categoria(request):
    saludar = "Hola, soy una categoría de este blog"
    return HttpResponse(saludar)

def home(request):
    hoy = datetime.now()
    saludo = f"""
    <html>
    <h1>bienvenido al home </h1>
    <h2> Hoy es {hoy} </h2>
    </html>
    """
    return HttpResponse(saludo)   