# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0002_auto_20160818_0052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=500)),
                ('location', models.CharField(blank=True, null=True, max_length=500)),
                ('description', models.CharField(blank=True, null=True, max_length=5000)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('registration_limit', models.PositiveSmallIntegerField(blank=True, default=10, null=True)),
                ('fee', models.DecimalField(blank=True, default=0, max_digits=255, null=True, decimal_places=2)),
                ('category', models.ManyToManyField(to='common.Category')),
            ],
            options={
                'ordering': ('start_time',),
                'get_latest_by': 'start_time',
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(null=True, auto_now_add=True)),
                ('paid', models.BooleanField(default=False)),
                ('attendee', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(to='event.Event')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
