# Generated by Django 5.0.4 on 2024-04-29 04:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nannies", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="nanny",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="nanny",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
