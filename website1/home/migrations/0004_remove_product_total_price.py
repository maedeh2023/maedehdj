# Generated by Django 5.0.3 on 2024-04-13 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_product_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='total_price',
        ),
    ]
