# Generated by Django 4.0.2 on 2022-02-28 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frankiesapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.TextField(max_length=300),
        ),
    ]
