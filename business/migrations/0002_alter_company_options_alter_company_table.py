# Generated by Django 5.0.1 on 2024-02-02 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={},
        ),
        migrations.AlterModelTable(
            name='company',
            table='business_Company',
        ),
    ]