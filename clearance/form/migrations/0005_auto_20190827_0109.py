# Generated by Django 2.2.4 on 2019-08-27 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0004_auto_20190823_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clearance',
            name='request',
            field=models.IntegerField(default=0),
        ),
    ]
