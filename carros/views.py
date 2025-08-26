from carros.models import Carro
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CarroModelForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

#Listar e Detalhar Carros:
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


#Adicionar, Atualizar e Deletar Carros:

@method_decorator(login_required(login_url='login'), name='dispatch')
class AddCarroCreateView(CreateView):
    model = Carro 
    form_class = CarroModelForm
    template_name = 'add_carro.html'
    success_url = '/lista/' 

class AtualizarCarroUpdateView(UpdateView):
    model = Carro 
    form_class = CarroModelForm
    template_name = 'atualizar_carro.html'

    def get_success_url(self):
        return reverse_lazy('detalhes_carros', kwargs={'pk': self.object.pk})
    
class DeletarCarroDeleteView(DeleteView):
    model = Carro 
    template_name = 'deletar_carro.html'
    success_url = '/lista/'
   