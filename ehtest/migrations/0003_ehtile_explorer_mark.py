# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-11-19 02:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehtest', '0002_auto_20161117_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='ehtile',
            name='explorer_mark',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
