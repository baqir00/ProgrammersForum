# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-24 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20170722_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='type',
            field=models.BooleanField(default=False),
        ),
    ]
