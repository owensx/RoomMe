# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0018_auto_20150308_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='img1',
            field=filer.fields.image.FilerImageField(blank=True, null=True, to='filer.Image', related_name='img1'),
            preserve_default=True,
        ),
    ]
