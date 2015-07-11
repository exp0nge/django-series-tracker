# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_auto_20150707_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='current_episode',
            field=models.IntegerField(default=1, help_text=b'Current episode you are on.'),
        ),
        migrations.AlterField(
            model_name='series',
            name='cover_image_url',
            field=models.URLField(help_text=b'Cover image URL.', blank=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='release_day',
            field=models.CharField(help_text=b'Release day, e.g., Monday', max_length=10, choices=[(b'MONDAY', b'Monday'), (b'TUESDAY', b'Tuesday'), (b'WEDNESDAY', b'Wednesday'), (b'THURSDAY', b'Thursday'), (b'FRIDAY', b'Friday'), (b'SATURDAY', b'Saturday'), (b'SUNDAY', b'Sunday'), (b'UNKNOWN', b'Unknown')]),
        ),
        migrations.AlterField(
            model_name='series',
            name='submitted_user',
            field=models.ForeignKey(default=django.contrib.auth.models.User, to=settings.AUTH_USER_MODEL),
        ),
    ]
