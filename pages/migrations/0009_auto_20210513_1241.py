# Generated by Django 3.0.5 on 2021-05-13 12:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20210513_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='can_book_call',
            name='date',
            field=models.DateField(verbose_name=datetime.datetime(2021, 5, 13, 12, 41, 36, 701188)),
        ),
    ]
