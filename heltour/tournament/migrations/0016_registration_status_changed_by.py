# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-23 23:38


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0015_auto_20160723_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='status_changed_by',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
