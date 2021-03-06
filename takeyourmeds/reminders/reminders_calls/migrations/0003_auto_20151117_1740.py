# -*- coding: utf-8 -*-
# Generated by Django 1.9c1 on 2015-11-17 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders_calls', '0002_auto_20151117_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='state',
            field=models.IntegerField(choices=[(10, b'twilio_disabled'), (20, b'failed'), (30, b'dialing'), (40, b'answered'), (50, b'busy'), (60, b'no_answer'), (70, b'unknown')], default=30),
        ),
        migrations.RunSQL("UPDATE reminders_calls_call SET state = state + 20"),
    ]
