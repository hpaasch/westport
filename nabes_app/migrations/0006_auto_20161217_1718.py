# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-17 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nabes_app', '0005_profile_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='check',
            field=models.CharField(default='please pay your dues', max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='paypal',
            field=models.CharField(default='please pay your dues', max_length=10),
        ),
    ]
