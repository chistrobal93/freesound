# Generated by Django 1.9.5 on 2017-01-16 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='display_amount',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='donation',
            name='is_anonymous',
            field=models.BooleanField(default=True),
        ),
    ]
