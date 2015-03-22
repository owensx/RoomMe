# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0005_auto_20150227_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='imgUrls',
            field=models.ImageField(upload_to=''),
            preserve_default=True,
        ),
    ]
