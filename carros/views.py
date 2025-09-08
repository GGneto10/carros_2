from carros.models import Carro,  MarcaCarro
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .forms import CarroModelForm
from django.db.models import Q, Count, Min, Max
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy 
from django.utils import timezone
from datetime import timedelta

#Listar e Detalhar Carros:
class CarrosListView(ListView): 
    model = Carro
    template_name = 'lista_carros.html' 
    context_object_name = 'carros'

    def get_queryset(self):
        carros = super().get_queryset().order_by('modelo')
        search = self.request.GET.get('search')

        if search:
            carros = carros.filter(
                Q(modelo__icontains=search) |
                Q(marca__name__icontains=search) |  
                Q(ano_fabricacao__icontains=search) |
                Q(ano_modelo__icontains=search) |
                Q(placa__icontains=search)
            ).order_by('modelo')
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
   
class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Busca simples (se houver)
        search_query = self.request.GET.get('search', '')
        
        # Carros em destaque (últimos 8 cadastrados)
        carros_destaque = Carro.objects.all().order_by('-id')[:8]
        
        # Ofertas especiais (carros mais baratos)
        carros_ofertas = Carro.objects.filter(valor__isnull=False).order_by('valor')[:6]
        
        # Carros com foto (para melhor visualização)
        carros_com_foto = Carro.objects.exclude(foto__isnull=True).exclude(foto='')[:12]
        
        # Marcas com mais carros
        marcas_populares = MarcaCarro.objects.annotate(
            total_carros=Count('marca_carro')
        ).filter(total_carros__gt=0).order_by('-total_carros')[:10]
        
        # Estatísticas para a home
        estatisticas = {
            'total_carros': Carro.objects.count(),
            'carros_com_foto': Carro.objects.exclude(foto__isnull=True).exclude(foto='').count(),
            'preco_minimo': Carro.objects.aggregate(Min('valor'))['valor__min'],
            'preco_maximo': Carro.objects.aggregate(Max('valor'))['valor__max'],
            'marca_mais_popular': MarcaCarro.objects.annotate(
                total=Count('marca_carro')
            ).order_by('-total').first(),
        }
        
         # Filtros recentes (últimos 6 meses)
        seis_meses_atras = timezone.now() - timedelta(days=180)
        carros_recentes = Carro.objects.filter(
            Q(ano_fabricacao__gte=timezone.now().year - 2) |
            Q(ano_modelo__gte=timezone.now().year - 2)
        )[:4]
        
        context.update({
            'carros_destaque': carros_destaque,
            'carros_ofertas': carros_ofertas,
            'carros_com_foto': carros_com_foto,
            'marcas_populares': marcas_populares,
            'carros_recentes': carros_recentes,
            'estatisticas': estatisticas,
            'search_query': search_query,
        })
        
        return context
    