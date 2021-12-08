# Generated by Django 3.2.9 on 2021-12-08 15:04

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores_api', '0003_alter_store_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='inventory',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, size=None),
        ),
    ]