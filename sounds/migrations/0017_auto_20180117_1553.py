# Generated by Django 1.11 on 2018-01-17 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sounds', '0016_merge_20171201_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packdownloadjson',
            name='pack',
        ),
        migrations.RemoveField(
            model_name='packdownloadjson',
            name='user',
        ),
        migrations.DeleteModel(
            name='PackDownloadJson',
        ),
    ]
