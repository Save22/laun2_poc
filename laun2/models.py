from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.pages.models import Page, RichText
from mezzanine.core.fields import FileField
# Create your models here.

class Category(Page, RichText):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class Promo(models.Model):
    promo_name = models.CharField(max_length=50)
    promo_category = models.ForeignKey(Category)
    promo_image = FileField(_('File'), max_length=200, upload_to="Promo Images", format='Image')

    def __str__(self):
        return self.promo_name


class SlideImage(Page):
    promo_slide = models.ForeignKey(Promo)
    slide_image = FileField(_('File'), max_length=200, upload_to="Banner Images", format='Image')
    caption = models.CharField(_('Caption'), blank=True, max_length=200)
