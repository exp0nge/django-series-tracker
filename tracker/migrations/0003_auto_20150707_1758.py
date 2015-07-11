# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracker', '0002_auto_20150707_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='series',
            name='sumbmitted_user',
        ),
        migrations.AddField(
            model_name='series',
            name='submitted_user',
            field=models.ForeignKey(default='', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
