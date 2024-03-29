# Generated by Django 4.0.4 on 2023-05-23 15:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_rename_user_postlike_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="slug",
            field=models.SlugField(
                default="2023/05/23", max_length=250, unique_for_date="created_time"
            ),
            preserve_default=False,
        ),
    ]
