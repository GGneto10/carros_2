from django.contrib import admin

from django.contrib import admin
from carros.models import Carro, MarcaCarro
from motos.models import Moto, MarcaMoto

class CarroAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'marca', 'ano_fabricacao', 'ano_modelo', 'valor', 'km', 'foto', 'cor', 'combustivel', 'portas', 'cambio') 
    search_fields = ('modelo', ) 

class MotoAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'marca', 'ano_fabricacao', 'ano_modelo', 'valor', 'km', 'foto', 'cor', 'combustivel', 'cilindradas', 'partida_eletrica') 
    search_fields = ('modelo', ) 

class MarcaCarroAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class MarcaMotoAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Carro, CarroAdmin) 
admin.site.register(MarcaCarro, MarcaCarroAdmin) 
admin.site.register(Moto, MotoAdmin)
admin.site.register(MarcaMoto, MarcaMotoAdmin)

