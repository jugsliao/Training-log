# Generated by Django 3.2.13 on 2022-07-26 13:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traininglog', '0031_alter_goal_goal_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='goal_date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='log',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]