# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 09:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mezzanine.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlideImage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Page')),
                ('slide_image', mezzanine.core.fields.FileField(max_length=200, verbose_name='File')),
                ('caption', models.CharField(blank=True, max_length=200, verbose_name='Caption')),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('pages.page',),
        ),
    ]
