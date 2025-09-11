from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Moto

class MotoModelForm(forms.ModelForm):
    # Campos adicionais com validações personalizadas
    ano_fabricacao = forms.IntegerField(
        required=False,
        validators=[
            MinValueValidator(1900, message="Ano de fabricação não pode ser anterior a 1900."),
            MaxValueValidator(2025, message="Ano de fabricação não pode ser futuro.")
        ],
        widget=forms.NumberInput(attrs={
            'min': '1900',
            'max': '2025',
            'placeholder': 'Ex: 2020'
        })
    )
    
    ano_modelo = forms.IntegerField(
        required=False,
        validators=[
            MinValueValidator(1900, message="Ano do modelo não pode ser anterior a 1900."),
            MaxValueValidator(2026, message="Ano do modelo não pode ser mais de 1 ano futuro.")
        ],
        widget=forms.NumberInput(attrs={
            'min': '1900',
            'max': '2026',
            'placeholder': 'Ex: 2021'
        })
    )
    
    valor = forms.FloatField(
        required=False,
        validators=[MinValueValidator(0, message="Valor não pode ser negativo.")],
        widget=forms.NumberInput(attrs={
            'step': '0.01',
            'min': '0',
            'placeholder': '0.00'
        })
    )
    
    km = forms.IntegerField(
        required=False,
        validators=[MinValueValidator(0, message="Quilometragem não pode ser negativa.")],
        widget=forms.NumberInput(attrs={
            'min': '0',
            'placeholder': '0'
        })
    )
    
    cilindradas = forms.IntegerField(
        required=False,
        validators=[
            MinValueValidator(50, message="Cilindradas mínima é 50cc."),
            MaxValueValidator(2000, message="Cilindradas máxima é 2000cc.")
        ],
        widget=forms.NumberInput(attrs={
            'min': '50',
            'max': '2000',
            'placeholder': 'Ex: 150, 300, 600'
        })
    )

    class Meta:
        model = Moto
        fields = '__all__'
        widgets = {
            'modelo': forms.TextInput(attrs={
                'placeholder': 'Ex: CG 160, Biz, Factor 125'
            }),
            'placa': forms.TextInput(attrs={
                'placeholder': 'Ex: ABC1D23 ou ABC1234',
                'oninput': "this.value = this.value.toUpperCase().replace(/[^A-Z0-9]/g, '').slice(0, 7)"
            }),
            'cor': forms.TextInput(attrs={
                'placeholder': 'Ex: Preto, Vermelho, Azul'
            }),
            'combustivel': forms.Select(choices=[
                ('', 'Selecione...'),
                ('Gasolina', 'Gasolina'),
                ('Etanol', 'Etanol'),
                ('Flex', 'Flex'),
                ('Elétrico', 'Elétrico'),
            ]),
            'foto': forms.FileInput(attrs={
                'accept': 'image/*',
                'class': 'custom-file-input'
            }),
        }
        labels = {
            'marca': 'Marca da Moto',
            'modelo': 'Modelo da Moto',
            'ano_fabricacao': 'Ano de Fabricação',
            'ano_modelo': 'Ano do Modelo',
            'km': 'Quilometragem (Km)',
            'cilindradas': 'Cilindradas (cc)',
            'partida_eletrica': 'Tem partida elétrica?',
        }
        help_texts = {
            'placa': 'Formato: ABC1D23 (Mercosul) ou ABC1234 (Antigo)',
            'foto': 'Formatos aceitos: JPG, PNG. Tamanho máximo: 5MB.',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ordenar marcas por nome
        self.fields['marca'].queryset = self.fields['marca'].queryset.order_by('name')
        # Adicionar classe CSS aos campos
        for field_name, field in self.fields.items():
            if field_name != 'partida_eletrica':
                field.widget.attrs['class'] = 'form-control'
    
    def clean_km(self):
        km = self.cleaned_data.get('km')
        if km is not None:
            if km < 0:
                raise forms.ValidationError('Quilometragem não pode ser negativa.')
            if km > 500000:
                raise forms.ValidationError('Quilometragem acima do possível para uma moto em condições de venda.')
        return km

    def clean_placa(self):
        placa = self.cleaned_data.get('placa', '')
        if placa:
            # Remover espaços e converter para maiúsculas
            placa = placa.strip().upper().replace(' ', '').replace('-', '')
            
            # Validar formato (Mercosul: AAA0A00 ou Antigo: AAA0000)
            if len(placa) not in [0, 7]:
                raise forms.ValidationError('A placa deve ter 7 caracteres.')
            
            if placa and not all(c.isalnum() for c in placa):
                raise forms.ValidationError('A placa deve conter apenas letras e números.')
                
        return placa

    def clean_ano_modelo(self):
        ano_fabricacao = self.cleaned_data.get('ano_fabricacao')
        ano_modelo = self.cleaned_data.get('ano_modelo')
        
        if ano_fabricacao and ano_modelo:
            if ano_modelo < ano_fabricacao:
                raise forms.ValidationError('Ano do modelo não pode ser anterior ao ano de fabricação.')
            if ano_modelo > ano_fabricacao + 1:
                raise forms.ValidationError('Ano do modelo não pode ser mais de 1 ano posterior ao ano de fabricação.')
        
        return ano_modelo

    def clean_valor(self):
        valor = self.cleaned_data.get('valor')
        if valor is not None and valor <= 0:
            raise forms.ValidationError('Valor deve ser maior que zero.')
        return valor

    def clean(self):
        cleaned_data = super().clean()
        # Validação cruzada entre ano de fabricação e ano do modelo
        ano_fabricacao = cleaned_data.get('ano_fabricacao')
        ano_modelo = cleaned_data.get('ano_modelo')
        
        if ano_fabricacao and ano_modelo and ano_modelo < ano_fabricacao:
            self.add_error('ano_modelo', 'Ano do modelo não pode ser anterior ao ano de fabricação.')
        
        return cleaned_data