# Generated by Django 4.0.2 on 2022-03-02 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frankiesapp', '0006_alter_product_product_visibility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_visibility',
            field=models.CharField(max_length=300),
        ),
    ]