# custom_tags.py

from django import template

register = template.Library()

@register.filter(name='get_star_range')
def get_star_range(value):
    return range(1, value + 1)

