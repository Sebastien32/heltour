# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-10-28 21:28


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0169_registration_section_preference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='section_preference',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tournament.Section'),
        ),
    ]
