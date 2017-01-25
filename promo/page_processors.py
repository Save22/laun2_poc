from mezzanine.pages.page_processors import processor_for
from .models import Category, Promo


@processor_for(Category, Promo)
def promo_list(request, page):
    promo = Promo.objects.filter(promo_category=page.category)
    return {
        'promo': promo,
        'category': Category.objects.all()
    }
