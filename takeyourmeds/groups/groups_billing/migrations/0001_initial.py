# -*- coding: utf-8 -*-
# Generated by Django 1.9c1 on 2015-11-28 18:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0003_auto_20151128_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='groups.Group')),
                ('stripe_customer_ident', models.CharField(max_length=255, unique=True)),
                ('plan', models.CharField(choices=[(1, b'Free plan')], max_length=40)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
