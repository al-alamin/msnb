# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0003_auto_20160623_0147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField(max_length=5000)),
                ('date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(to='models.Author')),
                ('category', models.ManyToManyField(to='models.Category')),
                ('tag', models.ManyToManyField(blank=True, to='models.Tag')),
            ],
        ),
    ]
