# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-10-09 17:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0165_auto_20170928_2049'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ['lichess_username'], 'permissions': (('invite_to_slack', 'Can invite to slack'), ('link_slack', 'Can manually link slack accounts'))},
        ),
    ]