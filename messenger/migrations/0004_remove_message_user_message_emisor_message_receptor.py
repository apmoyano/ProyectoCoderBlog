# Generated by Django 4.0.3 on 2022-04-26 02:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messenger', '0003_message_titulo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.AddField(
            model_name='message',
            name='emisor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='emisor', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='receptor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='receptor', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
