# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20160818_0052'),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='presenter',
            field=models.ForeignKey(default=1, to='common.Author'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registration',
            name='skype_id',
            field=models.CharField(max_length=255, default=1),
            preserve_default=False,
        ),
    ]
