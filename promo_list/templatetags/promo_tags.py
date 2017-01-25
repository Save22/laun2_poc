from mezzanine import template
from promo.models import Category


register = template.Library()


@register.assignment_tag
def get_categories():
    return Category.objects.all()
