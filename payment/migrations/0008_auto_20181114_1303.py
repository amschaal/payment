# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-14 21:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0007_auto_20181114_1302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='fid',
            new_name='account',
        ),
    ]