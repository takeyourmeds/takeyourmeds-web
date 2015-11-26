# -*- coding: utf-8 -*-
# Generated by Django 1.9c1 on 2015-11-23 13:56
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.crypto
import functools


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recordings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=200)),
                ('ident', models.CharField(default=functools.partial(django.utils.crypto.get_random_string, *(40,), **{}), max_length=40, unique=True)),
                ('twilio_sid', models.CharField(default=None, max_length=34, null=True, unique=True)),
                ('created', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('recording', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='recordings.Recording')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recording_create_requests', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
                'get_latest_by': 'created',
            },
        ),
    ]
