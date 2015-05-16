# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0002_delete_reminder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('crontab', models.CharField(max_length=100, blank=True)),
                ('message', models.CharField(max_length=100, blank=True)),
                ('phone_number', models.CharField(max_length=200)),
                ('last_run', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
