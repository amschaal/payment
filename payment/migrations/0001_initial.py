# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-10 00:19
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[(b'GENERIC', b'GENERIC')], default=b'GENERIC', max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[(b'UNPAID', b'Unpaid'), (b'PAID', b'Paid'), (b'PENDING', b'Payment Pending')], max_length=20)),
            ],
        ),
    ]
