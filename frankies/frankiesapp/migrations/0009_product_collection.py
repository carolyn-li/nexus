# Generated by Django 4.0.2 on 2022-03-02 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frankiesapp', '0008_merge_20220302_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productcollection_name', models.CharField(max_length=300)),
            ],
        ),
    ]
