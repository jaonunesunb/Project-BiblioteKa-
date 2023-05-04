# Generated by Django 4.1.7 on 2023-03-07 19:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=80)),
                ("author", models.CharField(max_length=40)),
                ("page_number", models.IntegerField()),
                ("publisher", models.CharField(max_length=40)),
                ("cdu", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Copy",
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
                ("buyed_at", models.DateField()),
                ("price", models.FloatField()),
                (
                    "sector",
                    models.CharField(
                        choices=[
                            ("general_collection", "General Collection"),
                            ("restauration", "Restauration"),
                            ("lost", "Lost"),
                            ("technical_treatment", "Technical Treatment"),
                        ],
                        default="general_collection",
                        max_length=20,
                    ),
                ),
                ("is_free", models.BooleanField(default=True)),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="copies",
                        to="books.book",
                    ),
                ),
            ],
        ),
    ]