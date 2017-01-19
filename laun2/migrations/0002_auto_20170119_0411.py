# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('laun2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slideimage',
            name='slide_image',
            field=mezzanine.core.fields.FileField(max_length=200, verbose_name='File'),
        ),
    ]
