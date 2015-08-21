# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20150819_0532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='creator',
            field=models.ForeignKey(to='creator.Creator'),
        ),
        migrations.DeleteModel(
            name='Creator',
        ),
    ]
