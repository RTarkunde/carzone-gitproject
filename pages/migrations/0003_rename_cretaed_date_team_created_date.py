# Generated by Django 3.2.12 on 2022-02-10 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_rename_teams_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='cretaed_date',
            new_name='created_date',
        ),
    ]
