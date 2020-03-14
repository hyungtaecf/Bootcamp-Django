from django import template

register = template.Library()

@register.filter(name='cut_the_string')
def cut_string(value, arg):
    """
    This cuts all values of "arg" from the string!
    """
    return value.replace(arg,'')

# register.filter('cut_the_string',cut_string)
