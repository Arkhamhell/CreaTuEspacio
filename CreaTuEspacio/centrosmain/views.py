from django.shortcuts import get_object_or_404, render
from centrosmain.models import Category, Centro , ImagenCentro

# Create your views here.

def list(request):

    centros = Centro.objects.all()
   

    return render(request , 'centros/list.html' , {
        'title' : 'Centros', 
        'centros' : centros
    })

def category(request , category_id):

    category = Category.objects.get(id = category_id)
    centros = Centro.objects.filter(categories = category_id)

    return render(request , 'categorias/category.html' , {
        'category' : category,
        

    })


def centros(request , centro_id):

    centro = get_object_or_404(Centro, id = centro_id)
    imagenesCentro = ImagenCentro.objects.filter(centro_id = centro_id)

    return render (request, 'centros/resena.html',{
        'centro' : centro ,
        'imagenes' : imagenesCentro
        
    })