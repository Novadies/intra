# Generated by Django 4.2.9 on 2024-02-26 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        (
            "loader",
            "0009_remove_testmodel_calcpress_remove_testmodel_calctemp_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="testmodel",
            name="to_user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="testmodel",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="testmodel1",
            name="to_user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="testmodel1",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
