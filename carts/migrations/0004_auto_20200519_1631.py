# Generated by Django 3.0.5 on 2020-05-19 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_auto_20200519_1626'),
    ]

    operations = [
        migrations.RenameField(
            model_name='copascart',
            old_name='Productos2',
            new_name='Productos',
        ),
    ]
