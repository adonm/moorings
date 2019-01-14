# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-10-22 23:11
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0090_auto_20181011_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReturnType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_descriptor', django.contrib.postgres.fields.jsonb.JSONField()),
                ('condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wildlifecompliance_condition', to='wildlifecompliance.ApplicationCondition')),
            ],
        ),
        migrations.AddField(
            model_name='return',
            name='condition',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='returns_condition', to='wildlifecompliance.ApplicationCondition'),
        ),
        migrations.AddField(
            model_name='return',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]