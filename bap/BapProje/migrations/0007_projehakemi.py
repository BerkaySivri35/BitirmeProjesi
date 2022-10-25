# Generated by Django 4.0.3 on 2022-06-17 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BapProje', '0006_belgeyukle'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjeHakemi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unvan', models.CharField(choices=[('Prof. Dr.', 'Prof. Dr.'), ('Doç. Dr.', 'Doç. Dr.'), ('Yrd. Doç. Dr.', 'Yrd. Doç. Dr.'), ('Dr. Öğr. Üyesi', 'Dr. Öğr. Üyesi'), ('Uzm. Dr.', 'Uzm. Dr.'), ('Dr.', 'Dr.'), ('Uzm.', 'Uzm.'), ('Arş. Gör.', 'Arş. Gör.'), ('Arş. Gör. Dr.', 'Arş. Gör. Dr.'), ('Öğr. Gör. Dr.', 'Öğr. Gör. Dr.'), ('Öğr. Gör.', 'Öğr. Gör.'), ('Öğrenci', 'Öğrenci'), ('Yüksek Lisans Öğrencisi', 'Yüksek Lisans Öğrencisi'), ('Doktora Öğrencisi', 'Doktora Öğrencisi'), ('Diğer', 'Diğer')], max_length=255)),
                ('adi', models.CharField(max_length=50)),
                ('soyadi', models.CharField(max_length=55)),
                ('universite', models.CharField(max_length=255)),
                ('fakulte', models.CharField(max_length=255)),
                ('bolum', models.CharField(max_length=255)),
                ('e_posta', models.EmailField(max_length=254)),
                ('telefon', models.CharField(max_length=11)),
            ],
        ),
    ]