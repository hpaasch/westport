# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-20 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nabes_app', '0013_auto_20161218_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='membership_status',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='resident_status',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='profile',
            name='number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='primary_last_name',
            field=models.CharField(default='required', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='primary_phone',
            field=models.CharField(default='required', max_length=12),
        ),
    ]
