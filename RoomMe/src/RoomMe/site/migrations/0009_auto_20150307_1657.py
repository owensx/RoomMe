# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0008_auto_20150307_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='img1',
            field=models.ImageField(upload_to='/static/imgs/listings/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='img10',
            field=models.ImageField(upload_to='/static/imgs/listings/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='img2',
            field=models.ImageField(upload_to='/static/imgs/listings/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='img3',
            field=models.ImageField(upload_to='/static/imgs/listings/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='img4',
            field=models.ImageField(upload_to='/static/imgs/listings/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='img5',
            field=models.ImageField(upload_to='/static/imgs/listings/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='img6',
            field=models.ImageField(upload_to='/static/imgs/listings/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='img7',
            field=models.ImageField(upload_to='/static/imgs/listings/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='img8',
            field=models.ImageField(upload_to='/static/imgs/listings/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listing',
            name='img9',
            field=models.ImageField(upload_to='/static/imgs/listings/', blank=True),
            preserve_default=True,
        ),
    ]
