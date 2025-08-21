from carros.models import Carro, Marca
from django.views.generic import ListView, DetailView
from django.db.models import Q

class CarrosListView(ListView): 
    model = Carro
    template_name = 'lista_carros.html' 
    context_object_name = 'carros'

    def get_queryset(self):
        carros = super().get_queryset().order_by('modelo')
        #esse "super" é uma função que acessa o pai dessa função. a classe neste caso.
        #ou seja, ela acessa o queryset do ListView e ordena os carros por modelo.
        #o mesmo que isso: cars = Car.objects.all().order_by('model')
        search = self.request.GET.get('search')

        if search:
            carros = carros.filter(
            Q(modelo__icontains=search) |
            Q(marca__icontains=search) |
            Q(ano_fabricacao__icontains=search) |
            Q(ano_modelo__icontains=search) |
            Q(placa__icontains=search)
        ).order_by('modelo') # Filtra em múltiplos campos usando Q objects para OR conditions
        return carros 
    
class CarrosDetailView(DetailView):
    model = Carro
    template_name = 'detalhes_carros.html'
