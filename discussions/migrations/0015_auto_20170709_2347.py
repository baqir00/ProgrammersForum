# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-09 18:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0014_auto_20170709_2346'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vote',
            options={'ordering': ['-QID', '-AID']},
        ),
    ]
