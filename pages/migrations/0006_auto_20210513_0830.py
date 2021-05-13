# Generated by Django 3.0.5 on 2021-05-13 08:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_login_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='can_book_call',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name=datetime.datetime(2021, 5, 13, 8, 30, 48, 164343))),
                ('booking_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='admin_model',
            name='advisor_id',
            field=models.IntegerField(default=0),
        ),
    ]
