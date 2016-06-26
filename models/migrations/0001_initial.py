# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('text', models.TextField(max_length=500)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('url', models.URLField()),
                ('bio', models.TextField(max_length=500)),
                ('thumbnail', models.ImageField(upload_to='images/', default='images/user_default.jpg')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('text', models.TextField(max_length=500)),
                ('date', models.DateField()),
                ('author', models.ForeignKey(to='models.Author')),
                ('category', models.ManyToManyField(to='models.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='questions',
            name='tag',
            field=models.ManyToManyField(to='models.Tag'),
        ),
        migrations.AddField(
            model_name='answers',
            name='author',
            field=models.ForeignKey(to='models.Author'),
        ),
        migrations.AddField(
            model_name='answers',
            name='category',
            field=models.ManyToManyField(to='models.Category'),
        ),
        migrations.AddField(
            model_name='answers',
            name='question',
            field=models.ForeignKey(to='models.Questions'),
        ),
        migrations.AddField(
            model_name='answers',
            name='tag',
            field=models.ManyToManyField(to='models.Tag'),
        ),
        migrations.AlterOrderWithRespectTo(
            name='answers',
            order_with_respect_to='question',
        ),
    ]
