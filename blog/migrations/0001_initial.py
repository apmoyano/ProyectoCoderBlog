# Generated by Django 4.0.3 on 2022-03-31 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Viajes',
            fields=[
                ('destino', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('pais', models.CharField(max_length=100)),
                ('anio', models.IntegerField()),
            ],
        ),
    ]