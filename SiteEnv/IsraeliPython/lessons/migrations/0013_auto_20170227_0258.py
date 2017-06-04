# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 00:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0012_auto_20170227_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_num',
            field=models.PositiveSmallIntegerField(db_index=True, default=0),
        ),
    ]
