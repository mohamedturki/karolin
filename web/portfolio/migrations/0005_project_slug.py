# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-13 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20151213_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
