# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-23 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_projectcategory_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='role',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='task',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
