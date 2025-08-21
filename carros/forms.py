from django import forms
from .models import Carro

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Carro
        fielsds = '__all__'

    def clean_km(self):
        km = self.cleaned_data.get('km')
        if km is not None:
            if km < 0:
                self.add_error('km', 'Quilometragem não pode ser negativa.')
        elif km > 500000:
                self.add_error('km', 'Quilometragem acima do possível a ser vendido.')
        return km
       