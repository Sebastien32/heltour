# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-24 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0141_auto_20170123_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaguedocument',
            name='allow_all_editors',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='seasondocument',
            name='allow_all_editors',
            field=models.BooleanField(default=False),
        ),
    ]