from django.shortcuts import render

def contacto(request):
    """Página de contacto e información de la agencia"""
    info = {
        'correo': 'contacto@tuagencia.com',
        'telefono': '+57 300 000 0000',
        'instagram': 'https://instagram.com/tuagencia',
        'facebook': 'https://facebook.com/tuagencia',
        'whatsapp': 'https://wa.me/573000000000'
    }
    return render(request, 'contacto/contacto.html', {'info': info})