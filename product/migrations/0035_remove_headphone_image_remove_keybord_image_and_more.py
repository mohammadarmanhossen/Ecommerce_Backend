# Generated by Django 5.1.3 on 2025-02-22 15:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0034_alter_review_headphone_alter_review_keybord'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headphone',
            name='image',
        ),
        migrations.RemoveField(
            model_name='keybord',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='review',
            name='headphone',
        ),
        migrations.RemoveField(
            model_name='review',
            name='keybord',
        ),
        migrations.AddField(
            model_name='headphone',
            name='image_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='keybord',
            name='image_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]
