# Generated by Django 3.2.13 on 2022-07-25 12:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traininglog', '0024_rename_goal_goal_goal_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='goal_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]