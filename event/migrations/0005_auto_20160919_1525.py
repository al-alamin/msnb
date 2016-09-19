# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20160919_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.CharField(max_length=30, help_text='For skype session select "skype_session".', default='skype_session', choices=[('skype_session', 'skype_session'), ('others', 'others')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registration',
            name='skype_id',
            field=models.CharField(max_length=255, help_text="required for 'skype session'."),
        ),
    ]
