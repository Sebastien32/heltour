# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-14 18:37


import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0137_auto_20170108_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='profile',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
