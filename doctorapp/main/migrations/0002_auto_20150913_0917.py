# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='date',
            field=main.models.CustomDateField(),
        ),
        migrations.AlterField(
            model_name='application',
            name='time',
            field=models.SmallIntegerField(choices=[(1, '09:00'), (2, '10:00'), (4, '11:00'), (8, '12:00'), (16, '13:00'), (32, '14:00'), (64, '15:00'), (128, '16:00'), (256, '17:00')]),
        ),
    ]
