# Generated by Django 3.0.5 on 2020-05-18 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0004_auto_20200518_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
