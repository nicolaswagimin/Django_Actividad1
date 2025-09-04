from django.shortcuts import render

def servicios(request):
    """Página de servicios y planes de viaje"""
    planes = [
        {'titulo': 'Plan Aventura', 'detalle': 'Trekking, rafting y actividades al aire libre.'},
        {'titulo': 'Plan Romántico', 'detalle': 'Hoteles boutique, cenas y experiencias para parejas.'},
        {'titulo': 'Plan Familiar', 'detalle': 'Actividades para niños y comodidades para toda la familia.'},
    ]
    return render(request, 'servicios/servicios.html', {'planes': planes})