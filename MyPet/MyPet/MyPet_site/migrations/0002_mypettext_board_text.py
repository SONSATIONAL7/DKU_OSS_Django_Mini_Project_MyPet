# Generated by Django 4.2.1 on 2023-05-16 20:48

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("MyPet_site", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="mypettext",
            name="board_text",
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]