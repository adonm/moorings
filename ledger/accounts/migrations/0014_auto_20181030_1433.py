# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-10-30 06:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20180207_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_addresses', to=settings.AUTH_USER_MODEL),
        ),
    ]