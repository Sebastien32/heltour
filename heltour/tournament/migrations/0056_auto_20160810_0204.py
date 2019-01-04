# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-10 02:04


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0055_auto_20160809_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='competitor_type',
            field=models.CharField(choices=[('team', 'Team'), ('individual', 'Individual')], default='team', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='league',
            name='pairing_type',
            field=models.CharField(choices=[('swiss-dutch', 'Swiss Tournament: Dutch Algorithm')], default='swiss-dutch', max_length=32),
            preserve_default=False,
        ),
    ]
