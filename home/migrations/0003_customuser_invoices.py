# Generated by Django 4.2.2 on 2023-09-01 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0018_reservation_comment'),
        ('home', '0002_customuser_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='invoices',
            field=models.ManyToManyField(blank=True, to='reservation.invoice'),
        ),
    ]