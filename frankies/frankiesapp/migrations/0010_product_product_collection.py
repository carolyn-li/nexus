# Generated by Django 4.0.2 on 2022-03-02 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frankiesapp', '0009_product_collection'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_collection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='frankiesapp.product_collection'),
        ),
    ]
