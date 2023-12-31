# Generated by Django 4.2.4 on 2023-09-10 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("finflo_app", "0008_category_is_default"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="default_group",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="default_users",
                to="finflo_app.group",
                verbose_name="Default Group",
            ),
        ),
    ]
