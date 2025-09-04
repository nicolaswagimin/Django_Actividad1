from django.shortcuts import render

def inicio(request):
    """Página principal de la agencia de turismo"""
    return render(request, 'inicio/inicio.html')