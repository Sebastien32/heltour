# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-04 05:09


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0048_auto_20160803_0311'),
    ]

    operations = [
        migrations.AddField(
            model_name='alternate',
            name='season_player',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='tournament.SeasonPlayer'),
        ),
        migrations.AlterUniqueTogether(
            name='alternate',
            unique_together=set([]),
        ),
        migrations.RunSQL('''
        UPDATE tournament_alternate alt SET season_player_id = (SELECT id FROM tournament_seasonplayer sp WHERE sp.season_id = alt.season_id AND sp.player_id = alt.player_id)
        ''')
    ]
