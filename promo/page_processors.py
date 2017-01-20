from mezzanine.pages.page_processors import processor_for
from .models import Category, Promo


@processor_for(Category, Promo)
def promo_list(request, page):
    promo = Promo.objects.filter(promo_category=page.category)
    return {
        'promo': promo
    }

@processor_for(Category, Promo)
def promo_list(request, page):
    promo_page = Promo.objects.filter(title=page.title)
    return {
        'promo_page': promo_page
    }
