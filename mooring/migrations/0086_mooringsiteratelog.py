# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-12-19 09:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mooring', '0085_bookingperiodoption_cancel_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='MooringsiteRateLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField(default=datetime.date.today)),
                ('date_end', models.DateField(blank=True, null=True)),
                ('details', models.TextField(blank=True, null=True)),
                ('booking_period', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='mooring.BookingPeriod')),
                ('mooringarea', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='marinearea', to='mooring.MooringArea')),
                ('reason', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mooring.PriceReason')),
            ],
        ),
    ]
