# Generated by Django 3.2.13 on 2022-06-26 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traininglog', '0004_auto_20220622_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log1',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]