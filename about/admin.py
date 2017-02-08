from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import About

admin.site.register(About, PageAdmin)
