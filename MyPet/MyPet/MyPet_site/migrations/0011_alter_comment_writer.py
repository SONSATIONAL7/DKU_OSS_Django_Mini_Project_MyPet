# Generated by Django 4.2.1 on 2023-05-17 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("MyPet_site", "0010_rename_comments_comment_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="writer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
