# Generated by Django 4.2.1 on 2023-05-16 21:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("MyPet_site", "0003_alter_mypettext_board_text"),
    ]

    operations = [
        migrations.AddField(
            model_name="mypettext",
            name="category",
            field=models.CharField(max_length=200, null=True),
        ),
    ]