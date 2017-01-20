from copy import deepcopy
from django.contrib import admin
from django.conf import settings

# Register your models here.

from promo.models import Category
from promo.models import Promo
from mezzanine.pages.admin import PageAdmin


class CategoryAdmin(admin.ModelAdmin):
    model = Category

    def has_module_permission(self, request):
        for (name, items) in settings.ADMIN_MENU_ORDER:
            if "promo.Category" in items:
                return True
        return False

class CategoryInline(admin.TabularInline):
    model = Category

class PromoAdmin(admin.ModelAdmin):
    model = Promo

    def has_module_permission(self, request):
        for (name, items) in settings.ADMIN_MENU_ORDER:
            if "promo.Promo" in items:
                return True
        return False

admin.site.register(Category, CategoryAdmin)
admin.site.register(Promo, PromoAdmin)
