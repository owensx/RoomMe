# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0002_auto_20150226_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomie',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
            preserve_default=True,
        ),
    ]
