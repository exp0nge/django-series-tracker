# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20150707_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='series',
            name='cover_image',
        ),
        migrations.AddField(
            model_name='series',
            name='cover_image_url',
            field=models.URLField(help_text=b'Cover image URL', blank=True),
        ),
    ]
