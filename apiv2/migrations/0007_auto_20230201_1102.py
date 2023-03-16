# Generated by Django 1.11.29 on 2023-02-01 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiv2', '0006_auto_20201230_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiv2client',
            name='status',
            field=models.CharField(choices=[('OK', 'Approved'), ('REJ', 'Rejected'), ('REV', 'Revoked'), ('PEN', 'Pending')], default='OK', max_length=3),
        ),
    ]
