# Generated by Django 3.0.5 on 2020-05-20 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0013_malteada'),
        ('carts', '0005_cart_totalc'),
    ]

    operations = [
        migrations.CreateModel(
            name='carMalteadas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('Productos', models.ManyToManyField(blank=True, null=True, to='Productos.Malteada')),
            ],
        ),
    ]
