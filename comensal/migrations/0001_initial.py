# Generated by Django 4.2.7 on 2023-11-19 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comensal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_comensal', models.CharField(max_length=40)),
                ('apellido_comensal', models.CharField(max_length=30)),
                ('genero', models.CharField(max_length=1)),
            ],
        ),
    ]
