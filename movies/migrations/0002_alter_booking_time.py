# Generated by Django 5.1.6 on 2025-03-04 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="time",
            field=models.CharField(
                choices=[
                    ("12:00:00", "12:00 PM"),
                    ("3:00:00", "3:00 PM"),
                    ("6:00:00", "6:00 PM"),
                    ("9:00:00", "9:00 PM"),
                ],
                max_length=8,
            ),
        ),
    ]
