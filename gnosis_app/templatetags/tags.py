from django import template

register = template.Library()


@register.filter(name='in_category')
def in_category(things, category):
    return things.filter(comment=category)


@register.filter(name='count_reply')
def count_reply(things, category):
    tt =  things.filter(comment=category)
    return tt.count()
