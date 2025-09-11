# motos/mixins.py
from motos.models import MarcaMoto

class MarcaMotoMixin:
    """Mixin para adicionar marcas de moto ao contexto"""
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marcas'] = MarcaMoto.objects.all().order_by('name')
        return context