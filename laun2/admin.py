from copy import deepcopy
from django.contrib import admin

from mezzanine.pages.admin import PageAdmin
from .models import Category, Promo, SlideImage

# Register your models here.

class CategoryAdmin(PageAdmin):
    model = Category

class PromoAdmin(admin.ModelAdmin):
    model = Promo
    list_display = (
        'id',
        'promo_name',
        'promo_category',
        'promo_image',
    )

class SlideImageAdmin(PageAdmin):
    model = SlideImage

admin.site.register(Category, CategoryAdmin)
admin.site.register(Promo, PromoAdmin)
admin.site.register(SlideImage, SlideImageAdmin)
