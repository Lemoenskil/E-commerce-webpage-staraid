from django import template

register = template.Library()

@register.filter
def has_rating(things, rating):
    return things.filter(rating=rating)
