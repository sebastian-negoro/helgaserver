# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 09:47
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('harbs', '0005_hockeymatch_created_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hockeymatch',
            name='match_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
