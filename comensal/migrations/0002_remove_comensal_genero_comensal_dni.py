# Generated by Django 4.2.7 on 2023-11-19 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comensal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comensal',
            name='genero',
        ),
        migrations.AddField(
            model_name='comensal',
            name='dni',
            field=models.CharField(default='00000000', max_length=8),
        ),
    ]
