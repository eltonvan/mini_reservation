# Generated by Django 4.2.2 on 2023-07-18 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0011_taxrate_tax_zone'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxrate',
            name='full_vat_rate',
            field=models.DecimalField(decimal_places=2, default=19, max_digits=5),
        ),
        migrations.AlterField(
            model_name='taxrate',
            name='tax_zone',
            field=models.CharField(default='Germany', max_length=255),
        ),
    ]
