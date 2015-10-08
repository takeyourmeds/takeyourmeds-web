# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import takeyourmeds.profile.utils


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('groups', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('user', models.OneToOneField(related_name='profile', primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(related_name='users', default=takeyourmeds.profile.utils.get_default_group, to='groups.Group')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
