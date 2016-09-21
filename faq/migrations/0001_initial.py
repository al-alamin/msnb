# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_auto_20160919_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('text', models.TextField(max_length=500)),
                ('ans', models.TextField(blank=True, max_length=500)),
                ('date', models.DateField(auto_now_add=True)),
                ('category', models.ManyToManyField(to='common.Category')),
                ('tag', models.ManyToManyField(to='common.Tag', blank=True)),
            ],
        ),
    ]
