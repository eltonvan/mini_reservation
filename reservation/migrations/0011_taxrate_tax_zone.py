# Generated by Django 4.2.2 on 2023-07-14 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0010_reservation_nationality'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxrate',
            name='tax_zone',
            field=models.CharField(default='DE', max_length=255),
        ),
    ]
