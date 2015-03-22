# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0009_auto_20150307_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='img1',
            field=models.ImageField(upload_to='/static/imgs/listings/blank.jpg', blank=True),
            preserve_default=True,
        ),
    ]
