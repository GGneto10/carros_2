from motos.models import Moto, MarcaMoto
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.views.generic import ListView
from django.db.models import Q

class MotosListView(ListView): 
    model = Moto
    template_name = 'lista_motos.html' 
    context_object_name = 'motos'

    def get_queryset(self):
        motos = super().get_queryset().order_by('modelo')
        search = self.request.GET.get('search')

        if search:
            motos = motos.filter(
                Q(modelo__icontains=search) |
                Q(marca__name__icontains=search) |  
                Q(ano_fabricacao__icontains=search) |
                Q(ano_modelo__icontains=search) |
                Q(placa__icontains=search)
            ).order_by('modelo')
        return motos
