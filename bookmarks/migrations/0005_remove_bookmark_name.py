# Generated by Django 3.2.17 on 2023-03-10 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0004_auto_20230206_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='name',
        ),
    ]