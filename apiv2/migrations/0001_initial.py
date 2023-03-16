# Generated by Django 1.9.5 on 2016-04-15 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiV2Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(blank=True, max_length=40)),
                ('status', models.CharField(choices=[(b'OK', b'Approved'), (b'REJ', b'Rejected'), (b'REV', b'Revoked'), (b'PEN', b'Pending')], default=b'OK', max_length=3)),
                ('name', models.CharField(max_length=64)),
                ('url', models.URLField()),
                ('redirect_uri', models.URLField()),
                ('description', models.TextField(blank=True)),
                ('accepted_tos', models.BooleanField(default=False)),
                ('allow_oauth_passoword_grant', models.BooleanField(default=False)),
                ('scope', models.CharField(choices=[(b'r', b'read'), (b'w', b'write'), (b'rw', b'read+write')], default=b'rw', max_length=3)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('throttling_level', models.IntegerField(default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apiv2_client', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
