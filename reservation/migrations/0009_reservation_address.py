# Generated by Django 4.2.2 on 2023-07-06 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0008_alter_taxrate_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
