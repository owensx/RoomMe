# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0016_auto_20150307_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='img1',
            field=models.ImageField(blank=True, upload_to='.'),
            preserve_default=True,
        ),
    ]
