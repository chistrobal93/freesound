# Generated by Django 1.11 on 2018-03-20 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sounds', '0019_remove_download_pack'),
    ]

    operations = [
        # Drop existing index for unique user_id/sound_id/pack_id (no longer used, and we don't want unique
        # sound_id/user_id either)
        migrations.RunSQL('drop index if exists sounds_download_user_id_key;'),

        # Drop existing indexs for pack downloads (now using another table)
        migrations.RunSQL('drop index if exists sounds_download_user_pack;'),
        migrations.RunSQL('drop index if exists sounds_download_created_with_pack_id_nn;'),
        migrations.RunSQL('drop index if exists sounds_download_pack_id_nn_created;'),

        # Drop index for sound downloads license as it was only used once to fill in license field
        migrations.RunSQL('drop index if exists sounds_download_license_id_sound_id;'),

        # Drop existing index for user downloads and create new one without unneeded "where pack_id is null" clause
        migrations.RunSQL('drop index if exists sounds_download_user_sound;'),
        migrations.RunSQL('create index "sounds_download_user_sound" on sounds_download(user_id, sound_id);'),
    ]
