# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-02 03:42


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0043_auto_20160802_0103'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlternateBucket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('board_number', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')])),
                ('min_rating', models.PositiveIntegerField(blank=True, null=True)),
                ('max_rating', models.PositiveIntegerField(blank=True, null=True)),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Season')),
            ],
        ),
        migrations.AlterField(
            model_name='alternate',
            name='board_number',
            field=models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], default=1),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='alternatebucket',
            unique_together=set([('season', 'board_number')]),
        ),
    ]
