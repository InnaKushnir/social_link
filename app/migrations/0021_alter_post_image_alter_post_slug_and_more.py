# Generated by Django 4.0.4 on 2023-05-31 16:55

import app.models
from django.db import migrations, models
import functools


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0020_alter_post_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=functools.partial(
                    app.models.post_image_file_path, *("posts",), **{}
                ),
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=functools.partial(
                    app.models.post_image_file_path, *("posts",), **{}
                ),
                verbose_name="Avatar",
            ),
        ),
    ]
