# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField(blank=True)),
                ('short_description', models.TextField(blank=True)),
                ('full_description', models.TextField(blank=True)),
                ('date', models.DateField(default=datetime.datetime.today)),
            ],
        ),
    ]
