# Generated by Django 2.0.9 on 2019-02-01 09:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0013_auto_20190201_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 1, 9, 45, 48, 862285, tzinfo=utc)),
        ),
    ]
