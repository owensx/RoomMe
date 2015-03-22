# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomie',
            name='id',
            field=models.AutoField(primary_key=True, default=0, serialize=False, auto_created=True, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='roomie',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
