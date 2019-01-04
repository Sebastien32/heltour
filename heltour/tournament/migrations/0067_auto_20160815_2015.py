# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-15 20:15


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0066_auto_20160814_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='loneplayerpairing',
            name='black_rank',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='loneplayerpairing',
            name='white_rank',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
