# Generated by Django 1.11 on 2017-07-10 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20170510_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_donation_email_sent',
            field=models.DateTimeField(db_index=True, default=None, null=True),
        ),
    ]
