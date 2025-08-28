from django import template

register = template.Library()

@register.filter(name='format_currency')
def format_currency(value):
    """Formata valor para padrão brasileiro: 120000.00 → '120.000,00'"""
    try:
        # Converte para float e depois para string formatada
        value = float(value)
        return f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except (ValueError, TypeError):
        return value

@register.filter(name='format_km')
def format_km(value):
    """Formata KM para padrão brasileiro: 120000 → '120.000'"""
    try:
        # Converte para inteiro e formata com separador de milhar
        value = int(value)
        return f"{value:,}".replace(",", ".")
    except (ValueError, TypeError):
        return value