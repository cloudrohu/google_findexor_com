# Generated by Django 5.0.1 on 2024-02-02 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_alter_company_options_alter_company_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
