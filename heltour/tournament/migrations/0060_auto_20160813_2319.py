# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-13 23:19


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0059_auto_20160813_2318'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LonePlayerPairing2',
            new_name='LonePlayerPairing',
        ),
        migrations.RenameModel(
            old_name='TeamPlayerPairing2',
            new_name='TeamPlayerPairing',
        ),
    ]
