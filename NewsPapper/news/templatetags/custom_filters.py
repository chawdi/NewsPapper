from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='censor')
def censor(value):
    censored_words = ['shit', 'fuck']
    for word in censored_words:
        value = value.replace(word, '*' * len(word))
    return mark_safe(value)


