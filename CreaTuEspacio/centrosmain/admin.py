from django.contrib import admin
from .models import Category, Centro , ImagenCentro


class ImagenCentroAdmin(admin.TabularInline):
   model = ImagenCentro

  

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at' ,)

class CentroAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at' , 'updated_at')
    inlines = [ImagenCentroAdmin]
    
    
# Register your models here.

admin.site.register(Category , CategoryAdmin)
admin.site.register(Centro, CentroAdmin)