# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20160919_1508'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('post_type', models.CharField(choices=[('blog', 'blog'), ('news', 'news')], max_length=30)),
                ('text', models.TextField(max_length=5000)),
                ('date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(to='common.Category')),
                ('tag', models.ManyToManyField(blank=True, to='common.Tag')),
            ],
        ),
    ]
