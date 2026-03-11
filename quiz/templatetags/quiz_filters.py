from django import template

register = template.Library()

@register.filter
def dict_get(dictionary, key):
    """Acessa um dicionário por chave no template"""
    if dictionary is None:
        return None
    return dictionary.get(key, [])

