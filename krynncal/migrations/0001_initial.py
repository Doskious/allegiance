# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-02 01:23
from __future__ import unicode_literals

from django.db import migrations, models
import krynncal.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CampaignDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_date', krynncal.fields.KrynnDateTimeField()),
            ],
        ),
    ]