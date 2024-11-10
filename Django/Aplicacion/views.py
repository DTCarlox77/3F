from django.shortcuts import render, HttpResponse, redirect
from .models import Fruta

def index(request):
    
    return render(request, "pages/index.html")

# Create your views here.
def main(request):
    
    return HttpResponse("<h1>Hola Mundo</h1>") # Retornamos un mensaje de Hola Mundo

def frutas(request):
    
    nombre = 'Marí'
    lista = ['Amarillo', 'Rojo', 'Azul', 'Verde']
    
    return render(request, 'pages/fruta.html', {
        'nombre' : nombre,
        'colores' : lista
    })

def fantasma(request):
    
    # Para redirigir a la URL con nombre de frutas
    return redirect('frutas')

def saludar(request, nombre):
    
    return HttpResponse(f'<h1>Hola, {nombre}.</h1>')

def formulario(request):
    
    listado_frutas = Fruta.objects.all()
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        descripcion = request.POST.get('descripcion')
        
        try:
            fruta = Fruta.objects.create(
                nombre = nombre,
                precio = precio,
                descripcion = descripcion
            )
        except Exception as e:
            print(f'Hubo un error: {e}')
        
    return render(request, 'pages/formulario.html', {
        'frutas' : listado_frutas
    })
    
def especifica(request, id):
    
    fruta = Fruta.objects.get(id=id)
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        fruta.nombre = nombre
        fruta.save()
    
    return render(request, 'pages/especifica.html', {
        'fruta' : fruta
    })
    
def eliminar(request, id):
    
    fruta = Fruta.objects.get(id=id)
    fruta.delete()
    
    return redirect('formulario')