# Generated by Django 4.1.3 on 2023-12-07 11:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0013_bukukreasi_buku_favorites_alter_buku_buku_favorites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bukukreasi',
            name='buku_favorites',
        ),
        migrations.AlterField(
            model_name='buku',
            name='buku_favorites',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
