# Generated by Django 5.1.1 on 2024-10-10 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0004_delete_cartitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]