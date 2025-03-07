# Generated by Django 5.1.6 on 2025-03-04 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Booking",
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
                ("movie_name", models.CharField(max_length=100)),
                ("number_of_tickets", models.IntegerField()),
                ("date", models.DateField()),
                (
                    "time",
                    models.CharField(
                        choices=[
                            ("12:00:00", "12:00 PM"),
                            ("14:00:00", "3:00 PM"),
                            ("16:00:00", "6:00 PM"),
                            ("18:00:00", "9:00 PM"),
                        ],
                        max_length=8,
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("contact_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=100)),
                ("message", models.TextField()),
            ],
        ),
    ]
