# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 03:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinci', '0005_auto_20161103_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='filter',
            name='height',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filter',
            name='width',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='height',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='width',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
