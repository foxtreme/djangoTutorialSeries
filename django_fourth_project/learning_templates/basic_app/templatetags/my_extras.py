from django import template

register = template.Library()


@register.filter(name='leave_out')
def leave_out(value, arg):
    """
    This cuts out all values of 'arg' from the string!
    :param value:
    :param arg:
    :return:
    """
    return value.lower().replace(arg, '')
