# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_auto_20170118_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonmodule',
            name='module_id',
            field=models.CharField(db_index=True, max_length=50),
        ),
    ]