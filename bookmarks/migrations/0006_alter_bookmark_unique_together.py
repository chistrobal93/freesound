# Generated by Django 3.2.17 on 2023-03-10 10:55

from django.conf import settings
from django.db import migrations

import logging

console_logger = logging.getLogger("console")


def remove_duplicate_bookmarks(apps, schema_editor):
    BookmarkCategory = apps.get_model("bookmarks", "BookmarkCategory")
    to_delete = []

    # Remove duplicates in categories
    for bookmark_category in BookmarkCategory.objects.all():
        already_seen_sound_ids = []
        for bookmark in bookmark_category.bookmarks.all():
            if bookmark.sound_id in already_seen_sound_ids:
                to_delete.append(bookmark)
            else:
                already_seen_sound_ids.append(bookmark.sound_id)

    # Remove duplicates without categories
    Bookmark = apps.get_model("bookmarks", "Bookmark")
    users_with_uncategorized_bookmarks = \
        list(set(Bookmark.objects.filter(category=None).values_list('user_id', flat=True)))
    for user_id in users_with_uncategorized_bookmarks:
        already_seen_sound_ids = []
        for bookmark in Bookmark.objects.filter(category=None, user_id=user_id):
            if bookmark.sound_id in already_seen_sound_ids:
                to_delete.append(bookmark)
            else:
                already_seen_sound_ids.append(bookmark.sound_id)

    console_logger.info(f"Will delete {len(to_delete)} bookmark objects")
    for bookmark in to_delete:
        bookmark.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('sounds', '0049_license_summary_for_describe_form'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookmarks', '0005_remove_bookmark_name'),
    ]

    operations = [
        migrations.RunPython(remove_duplicate_bookmarks, migrations.RunPython.noop),
        migrations.AlterUniqueTogether(
            name='bookmark',
            unique_together={('user_id', 'category_id', 'sound_id')},
        ),
    ]
