# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0007_auto_20170131_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonmodule',
            name='module_name',
            field=models.CharField(db_index=True, max_length=50),
        ),
    ]
