# Generated by Django 4.2.1 on 2023-05-17 10:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("MyPet_site", "0006_comment"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="petText",
            new_name="pet",
        ),
    ]
