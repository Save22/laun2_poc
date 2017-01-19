# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('category_name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('promo_name', models.CharField(max_length=50)),
                ('promo_image', mezzanine.core.fields.FileField(max_length=200, verbose_name='File')),
                ('promo_category', models.ForeignKey(to='laun2.Category')),
            ],
        ),
        migrations.CreateModel(
            name='SlideImage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('slide_image', models.ImageField(upload_to='Slide Image')),
                ('promo_slide', models.ForeignKey(to='laun2.Promo')),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('pages.page',),
        ),
    ]
