
from django import template

register = template.Library()
counter = 0
@register.filter
    

@register.filter
def list_index_from_value(list_, value):
    l = list(list_)
    
    return l.index(value)+1
