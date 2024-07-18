# custom_filters.py
from django import template
import decimal

register = template.Library()

@register.filter(name='get_range')
def get_range(value):
    return range(value)

@register.filter
def sub(value, arg):
    return value - arg

@register.filter
def make_range(value):
    return range(int(value))



register = template.Library()

@register.filter
def range_filter(value):
    return range(value)
# custom_filters.py

from django import template

register = template.Library()

@register.filter
def rating_to_int(value):
    return int(value)

# your_app/templatetags/myfilters.py
from django import template

register = template.Library()

@register.filter
def get_range(value):
    # Implement your custom filter logic here
    return range(value)  # Example implementation



import decimal



def get_range(value):
    if isinstance(value, (int, float)):
        return range(int(value))
    elif isinstance(value, decimal.Decimal):
        return range(int(round(value)))
    elif isinstance(value, str):
        try:
            return range(int(value))  # Attempt conversion if it's a string containing a number
        except ValueError:
            pass  # Ignore non-numeric strings (optional, handle differently if needed)
    else:
        raise ValueError("get_range filter expects an integer, float, decimal, or convertible string")


@register.filter(name='is_integer')
def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False





@register.filter
def make_range(value):
    try:
        if isinstance(value, int):
            return range(value)
        elif isinstance(value, float):
            return range(int(value))
        elif isinstance(value, decimal.Decimal):
            return range(int(value))
        else:
            return range(0)
    except:
        return range(0)

