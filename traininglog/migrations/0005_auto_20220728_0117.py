# Generated by Django 3.2.13 on 2022-07-27 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traininglog', '0004_auto_20220727_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='goal_daily',
            field=models.CharField(default='Run for 20 minutes', max_length=50),
        ),
        migrations.AlterField(
            model_name='goal',
            name='goal_description',
            field=models.CharField(default='Keep healthy', max_length=50),
        ),
    ]