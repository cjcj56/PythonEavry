# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0004_auto_20170122_2023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='lesson_id',
            new_name='lesson_num',
        ),
        migrations.AddField(
            model_name='lessonmodule',
            name='module_desc',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='lessonmodule',
            name='module_num',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
