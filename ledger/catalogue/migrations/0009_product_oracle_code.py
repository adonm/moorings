# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-01 00:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0008_auto_20160304_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='oracle_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
