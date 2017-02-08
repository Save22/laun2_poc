from __future__ import unicode_literals

from django.db import models
from mezzanine.pages.models import Page, RichText
from promo.models import Category


class Coupon(Page, RichText):
    coupon_category = models.ForeignKey(Category)
    coupon_image = models.ImageField(upload_to="Coupon Images")
