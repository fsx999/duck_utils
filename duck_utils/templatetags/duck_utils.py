# coding=utf-8
from django.template import Library

register = Library()

@register.filter
def get_range(value):
    return range(value)



