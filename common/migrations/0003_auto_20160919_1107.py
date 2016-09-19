# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20160919_1107'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0002_auto_20160818_0052'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMeta',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(null=True, blank=True)),
                ('short_bio', models.TextField(null=True, blank=True, max_length=200)),
                ('long_bio', models.TextField(null=True, blank=True, max_length=5000)),
                ('facebook_link', models.URLField(null=True, blank=True)),
                ('linkedin_link', models.URLField(null=True, blank=True)),
                ('twitter_link', models.URLField(null=True, blank=True)),
                ('gplus_link', models.URLField(null=True, blank=True)),
                ('thumbnail', models.ImageField(upload_to='images/', default='images/user_default.jpg')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),

        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='AuthorRole',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
