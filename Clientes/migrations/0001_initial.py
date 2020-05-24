# Generated by Django 3.0.5 on 2020-05-14 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('numero_contacto', models.IntegerField()),
                ('correo', models.EmailField(max_length=254)),
                ('contrasena', models.CharField(max_length=20)),
            ],
        ),
    ]
