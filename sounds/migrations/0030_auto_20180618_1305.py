# Generated by Django 1.11 on 2018-06-18 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sounds', '0029_merge_20180510_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulkuploadprogress',
            name='progress_type',
            field=models.CharField(choices=[(b'N', b'Not yet validated'), (b'F', b'Finished description'), (b'S', b'Sounds being described and processed'), (b'V', b'Finished validation'), (b'C', b'Closed')], default=b'N', max_length=1),
        ),
    ]
