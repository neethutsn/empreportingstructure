# Generated by Django 4.1.6 on 2023-02-12 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("emp_code", models.TextField(max_length=20)),
                ("emp_name", models.TextField(max_length=50)),
                ("emp_contact", models.TextField(max_length=20)),
                ("emp_cat", models.TextField(max_length=50)),
                ("emp_pwd", models.TextField(max_length=50)),
            ],
        ),
    ]
