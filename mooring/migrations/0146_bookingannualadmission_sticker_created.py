# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-08-05 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooring', '0145_auto_20200731_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingannualadmission',
            name='sticker_created',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]