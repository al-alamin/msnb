# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='tag',
            field=models.ManyToManyField(to='models.Tag', blank=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='bio',
            field=models.TextField(max_length=500, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='tag',
            field=models.ManyToManyField(to='models.Tag', blank=True),
        ),
    ]
