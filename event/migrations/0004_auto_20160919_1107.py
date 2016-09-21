# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20160820_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='presenter',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
