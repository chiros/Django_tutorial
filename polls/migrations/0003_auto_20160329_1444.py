# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-29 06:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20160329_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
