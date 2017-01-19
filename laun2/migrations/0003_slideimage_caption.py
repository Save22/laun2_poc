# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laun2', '0002_auto_20170119_0411'),
    ]

    operations = [
        migrations.AddField(
            model_name='slideimage',
            name='caption',
            field=models.CharField(max_length=200, verbose_name='Caption', blank=True),
        ),
    ]
