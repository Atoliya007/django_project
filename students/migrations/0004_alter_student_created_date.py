# Generated by Django 5.1.3 on 2024-11-30 11:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_student_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 30, 11, 21, 1, 812272)),
        ),
    ]
