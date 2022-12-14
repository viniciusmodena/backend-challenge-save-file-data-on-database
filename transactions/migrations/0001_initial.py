# Generated by Django 4.1.2 on 2022-10-07 15:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("transaction_types", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transactions",
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
                ("date", models.DateField()),
                ("value", models.DecimalField(decimal_places=2, max_digits=15)),
                ("cpf", models.CharField(max_length=11)),
                ("card_number", models.CharField(max_length=12)),
                ("time", models.TimeField()),
                ("store_owner", models.CharField(max_length=14)),
                ("store_name", models.CharField(max_length=19)),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="transations",
                        to="transaction_types.transactiontype",
                        to_field="type",
                    ),
                ),
            ],
        ),
    ]
