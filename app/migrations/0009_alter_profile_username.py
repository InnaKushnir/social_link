# Generated by Django 4.0.4 on 2023-05-25 15:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0008_profile_username_alter_postlike_unique_together"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="username",
            field=models.CharField(max_length=63, unique=True),
        ),
    ]
