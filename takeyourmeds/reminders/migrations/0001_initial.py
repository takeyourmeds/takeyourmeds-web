# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=100, blank=True)),
                ('audiourl', models.CharField(max_length=100, blank=True)),
                ('telnumber', models.CharField(max_length=200)),
                ('user', models.ForeignKey(related_name='reminders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cronstring', models.CharField(max_length=100, blank=True)),
                ('last_run', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('reminder', models.ForeignKey(related_name='times', to='reminders.Reminder')),
            ],
        ),
    ]
