# -*- coding: utf-8 -*-
# Generated by Django 1.9c1 on 2015-11-28 18:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.crypto
import functools


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_auto_20151128_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesstoken',
            name='access_token',
            field=models.CharField(default=functools.partial(django.utils.crypto.get_random_string, *(8, b'ACEFHKJMLNPRUTWVYX'), **{}), max_length=8, unique=True),
        ),
    ]
