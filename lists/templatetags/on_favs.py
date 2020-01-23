from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def on_favs(request, room):
    pass
