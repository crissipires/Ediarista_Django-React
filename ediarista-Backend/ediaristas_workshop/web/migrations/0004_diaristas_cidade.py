# Generated by Django 3.2.5 on 2021-07-15 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20210626_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='diaristas',
            name='cidade',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
