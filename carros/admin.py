from django.contrib import admin

from django.contrib import admin
from carros.models import Carro, Marca

class CarroAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'marca', 'ano_fabricacao', 'ano_modelo', 'valor', 'km') 
    search_fields = ('modelo', ) #buscar os modelos

class MarcaAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Carro, CarroAdmin) 
admin.site.register(Marca, MarcaAdmin) 

