from django.urls import path
from . import views
 


urlpatterns = [
    path('list/' , views.list , name="list"),
    path('categoria/<int:category_id>' , views.category , name="category"),
    path('centros/<int:centro_id>' , views.centros , name="centros")
]
