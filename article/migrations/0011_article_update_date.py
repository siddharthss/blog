# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_auto_20150820_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='update_date',
            field=models.DateField(default=datetime.datetime(2015, 8, 24, 9, 7, 59, 778438, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
