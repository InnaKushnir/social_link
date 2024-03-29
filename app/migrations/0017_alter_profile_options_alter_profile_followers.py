# Generated by Django 4.0.4 on 2023-05-28 16:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0016_alter_profile_user"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="profile",
            options={"ordering": ["username"]},
        ),
        migrations.AlterField(
            model_name="profile",
            name="followers",
            field=models.ManyToManyField(related_name="followed_by", to="app.profile"),
        ),
    ]
