# Generated by Django 3.2.4 on 2021-06-26 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_diaristas_cep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diaristas',
            name='bairro',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='diaristas',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
