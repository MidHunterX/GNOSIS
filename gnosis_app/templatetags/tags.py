from django import template
from django.template.defaultfilters import timesince

register = template.Library()


@register.filter(name='in_category')
def in_category(things, category):
    return things.filter(comment=category)


@register.filter(name='count_reply')
def count_reply(things, category):
    tt =  things.filter(comment=category)
    return tt.count()


@register.filter
def smol_timesince(value):
    natural_time = timesince(value)
    return natural_time.split(",")[0]


@register.filter(name='limit_iterations')
def limit_iterations(value, limit):
    return value[:limit]
