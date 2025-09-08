from django.db import models

class MarcaCarro(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

#indico pro django que essa classe vai ser um Modelo
class Carro(models.Model): 
    id = models.AutoField(primary_key=True) 
    modelo = models.CharField(max_length=200) 
    marca = models.ForeignKey(MarcaCarro, on_delete=models.PROTECT, related_name=('marca_carro')) 
    ano_fabricacao = models.IntegerField(blank=True, null=True) 
    ano_modelo = models.IntegerField(blank=True, null=True)
    placa = models.CharField(max_length=10, blank=True, null=True) 
    valor = models.FloatField(blank=True, null=True)
    km = models.IntegerField(blank=True, null=True)
    foto = models.ImageField(upload_to='carros/', blank=True, null=True)
    cor = models.CharField(max_length=50, blank=True, null=True)
    combustivel = models.CharField(max_length=50, blank=True, null=True)
    portas = models.IntegerField(blank=True, null=True)
    cambio = models.CharField(max_length=50, blank=True, null=True)

    
    
    def __str__(self):
        return self.modelo
