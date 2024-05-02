# Generated by Django 5.0.4 on 2024-05-02 04:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("nannies", "0003_nanny_deleted_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("deleted_at", models.DateTimeField(null=True)),
                (
                    "nanny",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="nannies.nanny"
                    ),
                ),
            ],
        ),
    ]
