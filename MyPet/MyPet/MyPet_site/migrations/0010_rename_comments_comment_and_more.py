# Generated by Django 4.2.1 on 2023-05-17 11:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("MyPet_site", "0009_rename_comment_comments"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Comments",
            new_name="Comment",
        ),
        migrations.RenameField(
            model_name="comment",
            old_name="comment",
            new_name="comments",
        ),
    ]
