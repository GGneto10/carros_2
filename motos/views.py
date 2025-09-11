from motos.models import Moto, MarcaMoto
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.views.generic import ListView
from django.db.models import Q
from .forms import MotoModelForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .mixins import MarcaMotoMixin

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

class MotosDetailView(DetailView):
    model = Moto
    template_name = 'detalhes_motos.html'

#Adicionar, Atualizar e Deletar Motos:

@method_decorator(login_required(login_url='login'), name='dispatch')
class AddMotoCreateView(MarcaMotoMixin, CreateView):
    model = Moto 
    form_class = MotoModelForm
    template_name = 'add_moto.html'
    success_url = '/lista_motos/'

'''
#Fazer a ADIÇÃO dos Templates, com Html, css e JS dps, e adicionar um href para o UpdateMotoView na detalhes_motos.html.


@method_decorator(login_required(login_url='login'), name='dispatch')
class UpdateMotoView(MarcaMotoMixin, UpdateView):
    model = Moto 
    form_class = MotoModelForm
    template_name = 'update_moto.html'
    success_url = '/lista_motos/'
'''