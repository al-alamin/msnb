# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_auto_20160919_1152'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
