# Generated by Django 5.0.7 on 2024-08-07 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0007_country_alter_address_options_book_published_country'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
    ]
