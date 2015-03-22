# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0014_auto_20150307_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='img1',
            field=models.ImageField(upload_to='.', blank=True),
            preserve_default=True,
        ),
    ]
