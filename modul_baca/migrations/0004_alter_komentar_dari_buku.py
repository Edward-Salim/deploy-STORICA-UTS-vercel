# Generated by Django 4.2.6 on 2023-10-25 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_buku_id_buku_buku_isi_buku'),
        ('modul_baca', '0003_alter_komentar_tgl_komentar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='komentar',
            name='dari_buku',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='komentar', to='main.buku'),
        ),
    ]