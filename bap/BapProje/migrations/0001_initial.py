# Generated by Django 4.0.3 on 2022-06-15 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasvuruKapak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_adi', models.CharField(choices=[('FEN', 'FEN'), ('EDEBİYAT', 'EDEBİYAT'), ('İİBF', 'İİBF'), ('MÜHENDİSLİK', 'MÜHENDİSLİK'), ('MİMARLIK', 'MİMARLIK')], max_length=255)),
                ('projenin_turu', models.CharField(choices=[('KAP', 'Kapsamlı Araştırma Projeleri'), ('YP', 'Yönlendirilmiş Proje'), ('LÖAOPYÜKSEKLİSANS', 'LİSANSÜSTÜ ÖĞRENİM ARAŞTIRMA PROJELERİ (YÜKSEK LİSANS)'), ('LÖAOPDOKTORA', 'LİSANSÜSTÜ ÖĞRENİM ARAŞTIRMA PROJELERİ (DOKTORA)'), ('KAP2', 'Katılımlı Araştırma Projeleri'), ('AYP', 'ALT YAPI PROJELERİ'), ('KUS', 'Kamu-Üniversite-Sanayi İşbirliği Projeleri'), ('UUKP', 'Ulusal ve Uluslararası Kaynaklı Projeler'), ('HDP', 'Hızlı Destek Projeleri')], max_length=255)),
                ('proje_basligi', models.CharField(max_length=255)),
                ('anahtar_kelimeler', models.CharField(max_length=255)),
                ('kurulus_adi', models.CharField(max_length=255)),
                ('proje_baslamaTarihi', models.DateField()),
                ('proje_suresi', models.IntegerField()),
                ('proje_sahibi_cv', models.FileField(upload_to='')),
            ],
        ),
    ]
