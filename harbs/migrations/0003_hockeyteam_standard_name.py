# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harbs', '0002_hockeyteam'),
    ]

    operations = [
        migrations.AddField(
            model_name='hockeyteam',
            name='standard_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]