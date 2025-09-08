from django.db import models

class MarcaMoto(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Moto(models.Model):
    id = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=200)
    marca = models.ForeignKey(MarcaMoto, on_delete=models.PROTECT, related_name=('marca_moto'))
    ano_fabricacao = models.IntegerField(blank=True, null=True)
    ano_modelo = models.IntegerField(blank=True, null=True)
    placa = models.CharField(max_length=10, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    km = models.IntegerField(blank=True, null=True)
    foto = models.ImageField(upload_to='motos/', blank=True, null=True)
    cor = models.CharField(max_length=50, blank=True, null=True)
    combustivel = models.CharField(max_length=50, blank=True, null=True)
    cilindradas = models.IntegerField(blank=True, null=True)
    partida_eletrica = models.BooleanField(default=False)

    def __str__(self):
        return self.modelo