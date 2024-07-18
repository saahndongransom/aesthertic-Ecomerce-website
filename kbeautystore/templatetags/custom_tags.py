# custom_tags.py

from django import template

register = template.Library()

@register.simple_tag
def star_range(rating):
    return range(1, rating + 1)
