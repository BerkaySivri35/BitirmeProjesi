# Generated by Django 4.0.3 on 2022-06-17 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BapProje', '0004_alter_projepersoneli_gorev_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projepersoneli',
            name='gorev',
            field=models.CharField(choices=[('Araştırmacı', 'Araştırmacı'), ('Danışman', 'Danışman'), ('Bursiyer', 'Bursiyer')], max_length=255),
        ),
    ]
