from django.contrib import admin

from mezzanine.pages.admin import PageAdmin
from .models import SlideImage

# Register your models here.


class SlideImageAdmin(PageAdmin):
    model = SlideImage

admin.site.register(SlideImage, SlideImageAdmin)
