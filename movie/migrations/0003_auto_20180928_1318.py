# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-28 03:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20180928_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='released',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
