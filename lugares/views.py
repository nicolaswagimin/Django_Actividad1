from django.shortcuts import render

def lugares(request):
    """Página de destinos turísticos"""
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
    return render(request, 'lugares/lugares.html', {'destinos': destinos})