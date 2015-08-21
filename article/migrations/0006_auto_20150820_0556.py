# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20150819_1247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='creator',
            new_name='user_id',
        ),
    ]
