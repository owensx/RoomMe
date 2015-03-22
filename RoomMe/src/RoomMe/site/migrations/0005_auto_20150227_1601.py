# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0004_auto_20150226_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='imgUrls',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
