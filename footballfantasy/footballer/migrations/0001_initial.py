# Generated by Django 4.2 on 2023-04-07 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Club",
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
                ("name", models.CharField(max_length=100)),
                ("country", models.CharField(max_length=100)),
                ("division", models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name="Footballer",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("nick_name", models.CharField(max_length=120)),
                ("date_of_birth", models.DateField()),
                ("position", models.IntegerField(blank=True)),
                ("jersy_number", models.IntegerField(blank=True)),
                ("market_value", models.IntegerField(blank=True)),
                (
                    "club",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="footballer.club",
                    ),
                ),
            ],
        ),
    ]
