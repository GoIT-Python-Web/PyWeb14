# Generated by Django 4.2.5 on 2023-09-20 18:07

from django.db import migrations, models
import instagram.models


class Migration(migrations.Migration):
    dependencies = [
        ("instagram", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(
                null=True, upload_to=instagram.models.update_filename
            ),
        ),
    ]
