# Generated by Django 4.0.3 on 2022-04-29 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_imagen_post_picture'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Categoria',
        ),
    ]
