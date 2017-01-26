from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.pages.models import Page
from mezzanine.core.fields import FileField
# Create your models here.


class SlideImage(Page):
    slide_image = FileField(
            _('File'),
            max_length=200,
            upload_to="Banner Images",
            format='Image'
    )
    caption = models.CharField(_('Caption'), blank=True, max_length=200)
