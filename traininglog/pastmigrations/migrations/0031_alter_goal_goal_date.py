# Generated by Django 3.2.13 on 2022-07-26 13:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traininglog', '0030_alter_goal_goal_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='goal_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]