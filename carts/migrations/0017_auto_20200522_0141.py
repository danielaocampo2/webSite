# Generated by Django 3.0.5 on 2020-05-22 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0016_auto_20200522_0121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='items',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
