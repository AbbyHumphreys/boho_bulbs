# Generated by Django 3.2.23 on 2023-12-09 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20231209_1828'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]