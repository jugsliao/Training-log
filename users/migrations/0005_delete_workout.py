# Generated by Django 3.2.13 on 2022-07-24 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_profile_workout'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Workout',
        ),
    ]