# Generated by Django 2.0.9 on 2019-01-05 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_auto_20190105_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(default='fremgangsmate'),
        ),
    ]
