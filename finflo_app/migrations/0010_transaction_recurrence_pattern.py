# Generated by Django 4.2.4 on 2023-09-10 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("finflo_app", "0009_alter_userprofile_default_group"),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="recurrence_pattern",
            field=models.CharField(
                choices=[("monthly", "Monthly")], default="once", max_length=20
            ),
        ),
    ]
