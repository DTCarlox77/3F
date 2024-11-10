from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import User

# Create your views here.
def main(request):
    
    return render(request, 'pages/main.html')

def login_view(request):
    
    mensaje = None
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                mensaje = 'Credenciales incorrectas'
        except Exception as e:
            print(f'Error al iniciar sesión')

    return render(request, 'pages/login.html', {
        'mensaje' : mensaje
    })
    
def register_view(request):
    
    mensaje = None
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if password != password2:
            mensaje = 'Las contraseñas no coinciden'

        elif username == 'pedro':
            print('error')
        
        else:
            try:
                user = User.objects.create_user(username=username, password=password)
                return redirect('login')
            except Exception as e:
                mensaje = 'No se pudo crear al usuario.'
    
    return render(request, 'pages/register.html', {
        'mensaje': mensaje
    })
    
def logout_view(request):
    
    logout(request)
    return redirect('login')

@login_required
def protegida(request):
    
    return HttpResponse(f'<h1>¡Hola, {request.user.username}!</h1>')