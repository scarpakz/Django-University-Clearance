# Generated by Django 2.2.4 on 2019-08-23 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clearance',
            name='request',
            field=models.IntegerField(default=0, max_length=3),
        ),
    ]
