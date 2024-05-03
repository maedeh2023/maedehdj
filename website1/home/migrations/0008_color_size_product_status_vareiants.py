# Generated by Django 5.0.3 on 2024-04-20 12:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_catgory_sub_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(blank=True, choices=[('None', 'none'), ('Size', 'size'), ('Color', 'color')], max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Vareiants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.PositiveIntegerField()),
                ('unit_price', models.PositiveIntegerField()),
                ('discount', models.PositiveIntegerField(blank=True, null=True)),
                ('color_variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.color')),
                ('product_variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
                ('size_variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.size')),
            ],
        ),
    ]
