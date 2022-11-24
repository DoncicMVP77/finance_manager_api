# Generated by Django 4.1.3 on 2022-11-15 05:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_alter_budget_date_create_alter_category_date_create_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 15, 8, 12, 40, 512395), verbose_name='Time of create'),
        ),
        migrations.AlterField(
            model_name='category',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 15, 8, 12, 40, 512395), verbose_name='Time of create'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 15, 8, 12, 40, 512395), verbose_name='Time of create'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 15, 8, 12, 40, 512395), verbose_name='Time of create'),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 15, 8, 12, 40, 512395), verbose_name='Time of create'),
        ),
    ]