# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-14 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nabes_app', '0004_profile_primary_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='number',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
