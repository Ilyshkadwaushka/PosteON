# Generated by Django 4.0 on 2022-01-03 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Публикация', 'verbose_name_plural': 'Публикации'},
        ),
    ]
