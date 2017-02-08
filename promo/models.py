from __future__ import unicode_literals

from django.db import models
from mezzanine.pages.models import Page, RichText


class Category(Page, RichText):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Promo(Page, RichText):
    promo_category = models.ForeignKey(Category)
    promo_image = models.ImageField(upload_to="Promo Images")
