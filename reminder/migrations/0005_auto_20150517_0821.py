# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0004_auto_20150516_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReminderTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cronstring', models.CharField(max_length=100, blank=True)),
                ('last_run', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='reminder',
            name='cronstring',
        ),
        migrations.RemoveField(
            model_name='reminder',
            name='last_run',
        ),
        migrations.AddField(
            model_name='remindertime',
            name='reminder',
            field=models.ForeignKey(to='reminder.Reminder'),
        ),
    ]
