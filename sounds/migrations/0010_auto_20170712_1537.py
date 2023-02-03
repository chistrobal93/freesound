# Generated by Django 1.11 on 2017-07-12 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sounds', '0009_download_license'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoundLicenseHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('license', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sounds.License')),
            ],
        ),
        migrations.AddField(
            model_name='soundlicensehistory',
            name='sound',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sounds.Sound'),
        ),
    ]
