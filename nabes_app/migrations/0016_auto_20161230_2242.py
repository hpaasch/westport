# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-30 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nabes_app', '0015_auto_20161226_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicpost',
            name='body',
            field=models.TextField(max_length=900),
        ),
    ]
