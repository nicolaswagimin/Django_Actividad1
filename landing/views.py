from django.shortcuts import render


def inicio(request):
    return render(request, 'landing/inicio.html')


def lugares(request):
    destinos = [
        {
            'nombre': 'Cartagena de Indias',
            'imagen': 'https://images.unsplash.com/photo-1519681393784-d120267933ba?q=80&w=1200&auto=format&fit=crop',
            'resena': 'Ciudad amurallada, historia colonial y playas del Caribe.'
        },
        {
            'nombre': 'Cusco y Machu Picchu',
            'imagen': 'https://images.unsplash.com/photo-1548791623-2f69b90c13b4?q=80&w=1200&auto=format&fit=crop',
            'resena': 'Maravilla del mundo y cultura inca en los Andes peruanos.'
        },
        {
            'nombre': 'Bariloche',
            'imagen': 'https://images.unsplash.com/photo-1542042161784-26ab9e041e5a?q=80&w=1200&auto=format&fit=crop',
            'resena': 'Lagos, montañas y chocolate en la Patagonia argentina.'
        },
    ]
    return render(request, 'landing/lugares.html', {'destinos': destinos})


def servicios(request):
    planes = [
        {'titulo': 'Plan Aventura', 'detalle': 'Trekking, rafting y actividades al aire libre.'},
        {'titulo': 'Plan Romántico', 'detalle': 'Hoteles boutique, cenas y experiencias para parejas.'},
        {'titulo': 'Plan Familiar', 'detalle': 'Actividades para niños y comodidades para toda la familia.'},
    ]
    return render(request, 'landing/servicios.html', {'planes': planes})


def contacto(request):
    info = {
        'correo': 'contacto@tuagencia.com',
        'telefono': '+57 300 000 0000',
        'instagram': 'https://instagram.com/tuagencia',
        'facebook': 'https://facebook.com/tuagencia',
        'whatsapp': 'https://wa.me/573000000000'
    }
    return render(request, 'landing/contacto.html', {'info': info})
