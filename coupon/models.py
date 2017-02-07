from __future__ import unicode_literals

# Create your models here.
from django.db import models
from mezzanine.pages.models import Page, RichText

class Category(Page, RichText):
    category_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.category_name

class Coupon(Page, RichText):
    coupon_category = models.ForeignKey(Category)
    coupon_image = models.ImageField(upload_to = "Coupon Images")

