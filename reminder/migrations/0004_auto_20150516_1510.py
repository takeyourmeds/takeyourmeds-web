# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0003_reminder'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reminder',
            old_name='crontab',
            new_name='cronstring',
        ),
        migrations.RenameField(
            model_name='reminder',
            old_name='phone_number',
            new_name='telnumber',
        ),
        migrations.AddField(
            model_name='reminder',
            name='audiourl',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
