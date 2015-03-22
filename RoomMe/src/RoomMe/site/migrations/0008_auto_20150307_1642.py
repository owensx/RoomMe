# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0007_auto_20150227_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='imgUrls',
        ),
        migrations.AddField(
            model_name='listing',
            name='img1',
            field=models.ImageField(blank=True, upload_to=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='listing',
            name='img10',
            field=models.ImageField(blank=True, upload_to=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='listing',
            name='img2',
            field=models.ImageField(blank=True, upload_to=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='listing',
            name='img3',
            field=models.ImageField(blank=True, upload_to=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='listing',
            name='img4',
            field=models.ImageField(blank=True, upload_to=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='listing',
            name='img5',
            field=models.ImageField(blank=True, upload_to=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='listing',
            name='img6',
            field=models.ImageField(blank=True, upload_to=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='listing',
            name='img7',
            field=models.ImageField(blank=True, upload_to=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='listing',
            name='img8',
            field=models.ImageField(blank=True, upload_to=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='listing',
            name='img9',
            field=models.ImageField(blank=True, upload_to=''),
            preserve_default=True,
        ),
    ]
