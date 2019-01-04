# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-08-03 22:18


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0158_auto_20170801_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerwarning',
            name='type',
            field=models.CharField(choices=[('unresponsive', 'Unresponsive'), ('card', 'Card')], max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='playerwarning',
            unique_together=set([('round', 'player', 'type')]),
        ),
    ]
