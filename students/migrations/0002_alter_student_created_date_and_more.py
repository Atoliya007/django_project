# Generated by Django 5.1.3 on 2024-11-30 10:08

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 30, 10, 8, 28, 496136)),
        ),
        migrations.AlterField(
            model_name='student',
            name='updated_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]