from django import template

register = template.Library()

@register.filter(name="modulo")
def modulo(self):
    # in our case x=4 and y=3
    return self % 4 == 3
    