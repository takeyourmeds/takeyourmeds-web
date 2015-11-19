# -*- coding: utf-8 -*-
# Generated by Django 1.9c1 on 2015-11-19 13:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.crypto
import functools


class Migration(migrations.Migration):

    dependencies = [
        ('reminders_calls', '0005_auto_20151119_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='button_pressed',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='call',
            name='ident',
            field=models.CharField(default=functools.partial(django.utils.crypto.get_random_string, *(40,), **{}), max_length=40, unique=True),
        ),
    ]