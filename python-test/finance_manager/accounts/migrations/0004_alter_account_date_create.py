# Generated by Django 4.1.3 on 2022-11-15 05:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_date_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 15, 8, 12, 40, 512395), verbose_name='Time of create'),
        ),
    ]
