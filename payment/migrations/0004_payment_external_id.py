# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-13 23:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_auto_20181113_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='external_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
