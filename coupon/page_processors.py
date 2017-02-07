from mezzanine.pages.page_processors import processor_for
from .models import Category, Coupon


@processor_for(Category, Coupon)
def coupon_list(request, page):
    coupon = Coupon.objects.filter(coupon_category=page.category)
    return {
        'coupon': coupon,
    }
