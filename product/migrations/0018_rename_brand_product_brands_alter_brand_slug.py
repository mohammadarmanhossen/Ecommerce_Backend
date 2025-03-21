# Generated by Django 5.1.3 on 2025-02-04 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_alter_product_brand'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='brand',
            new_name='brands',
        ),
        migrations.AlterField(
            model_name='brand',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
