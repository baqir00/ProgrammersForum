# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-14 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0002_auto_20170412_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='QID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]