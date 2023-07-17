# Generated by Django 4.2.2 on 2023-07-17 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("reservation", "0013_invoice"),
        ("home", "0002_customuser_city"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="tax_rate_id",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="reservation.taxrate",
            ),
        ),
    ]
