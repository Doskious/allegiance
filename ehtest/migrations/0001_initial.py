# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-11-18 00:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ehEdgePart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_cardinality', models.IntegerField(choices=[('NORTH', 0), ('EAST', 1), ('SOUTH', 2), ('WEST', 3)], default=0)),
                ('change_size', models.BooleanField(default=False)),
                ('connected_to', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='connected_from', to='ehtest.ehEdgePart')),
            ],
        ),
        migrations.CreateModel(
            name='ehExplorer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=1)),
                ('size', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ehTile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('special', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='ehexplorer',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='explorers', to='ehtest.ehTile'),
        ),
        migrations.AddField(
            model_name='ehedgepart',
            name='parent_tile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='edges', to='ehtest.ehTile'),
        ),
    ]
