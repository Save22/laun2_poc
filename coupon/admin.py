from django.contrib import admin
from django.conf import settings

# Register your models here.
from coupon.models import Coupon
from coupon.models import Category
from mezzanine.pages.admin import PageAdmin

class CategoryAdmin(admin.ModelAdmin):
    model = Category

    def has_module_permission(self, request):
        for (name, items) in settings.ADMIN_MENU_ORDER:
            if "coupon.Category" in items:
                return True
        return False

class CouponAdmin(admin.ModelAdmin):
    model = Coupon

    def has_module_permission(self, request):
        for (name, items) in settings.ADMIN_MENU_ORDER:
            if "coupon.Coupon" in items:
                return True
        return False

admin.site.register(Coupon, CouponAdmin)
admin.site.register(Category, CategoryAdmin)
