# Generated by Django 4.2.3 on 2024-02-17 13:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("loader", "0004_uploadfiles_to_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="uploadfiles",
            name="time",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
