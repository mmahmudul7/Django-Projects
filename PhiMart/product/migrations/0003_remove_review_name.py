# Generated by Django 5.1.6 on 2025-03-18 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_options_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='name',
        ),
    ]
