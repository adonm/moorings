# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-11 02:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('disturbance', '0017_compliancelogdocument'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=200)),
                ('text', models.TextField(blank=True)),
                ('compliance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disturbance.Compliance')),
                ('officer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]