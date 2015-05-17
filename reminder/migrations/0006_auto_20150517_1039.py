# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reminder', '0005_auto_20150517_0821'),
    ]

    operations = [
        migrations.AddField(
            model_name='reminder',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='remindertime',
            name='reminder',
            field=models.ForeignKey(related_name='reminder_times', to='reminder.Reminder'),
        ),
    ]
