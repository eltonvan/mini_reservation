# Generated by Django 4.2.2 on 2023-07-18 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0015_invoice_invoice_netto'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='invoice_citytax',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='invoice_number_of_nights',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='invoice_vat',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
